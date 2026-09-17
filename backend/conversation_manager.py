from memory_manager import memory_manager
from context_extractor import extract_environmental_data
from context_validator import validate_context
from reasoning_engine import generate_recommendation
from rag.rag_engine import retrieve_scientific_evidence, co
import json

class ConversationManager:
    def process_turn(self, session_id: str, user_message: str) -> dict:
        print(f"🔄 Processing Turn for Session: {session_id}")
        
        # 1. Get user's session history
        session = memory_manager.get_session(session_id)
        session.add_message("user", user_message)

        # 2. Extract Data from Message (using LLM)
        extracted_data = extract_environmental_data(user_message)
        
        # 3. Update Memory Context
        if extracted_data:
            session.update_context(extracted_data)

        context_dict = session.context.model_dump()

        # 4. Smart Intent Check: Is this a direct factual question / document retrieval query?
        is_direct_question = any(q in user_message.lower() for q in ["what", "why", "how", "tell", "explain", "value", "?"])
        
        # Retrieve evidence specifically prioritizing this session's uploaded docs
        evidence = retrieve_scientific_evidence(user_message, session.context, top_k=3, session_id=session_id)

        # If it's a direct question and we found evidence, answer directly without blocking on missing context variables!
        if is_direct_question and evidence:
            print("💡 Direct Factual Query detected. Answering directly from retrieved document evidence...")
            
            evidence_text = "\n\n".join([f"Source: {e.get('title')} ({e.get('organization')})\nContent: {e.get('fact')}" for e in evidence])
            
            prompt = f"""You are Darukaa AI, an environmental intelligence assistant. Answer the user's question directly and accurately based ONLY on the provided evidence chunks below. Do not force an environmental assessment or ask for missing soil/climate variables if the user is simply asking a direct factual question. Include source attribution.

Evidence:
{evidence_text}

User Question: {user_message}

Answer:"""

            try:
                response = co.chat(
                    model="command",
                    message=prompt,
                    temperature=0.1
                )
                reply = response.text
            except Exception:
                # Fallback if chat model naming differs
                reply = evidence[0].get('fact')

            # Format sources cleanly
            if evidence:
                reply += "\n\n📚 **Evidence & Authoritative Sources:**\n"
                for src in evidence:
                    reply += f"- **{src.get('organization')}**: *{src.get('title')}* ([Link]({src.get('url')}))\n"

            session.add_message("assistant", reply)

            return {
                "reply": reply,
                "updated_context": context_dict,
                "is_recommendation": False
            }

        # 5. Otherwise, proceed with standard Validation & Recommendation flow (Untouched)
        validation_result = validate_context(context_dict)

        if not validation_result["is_sufficient"]:
            print("⚠️ Context Insufficient. Asking clarification question...")
            reply = validation_result["clarification_question"]
            session.add_message("assistant", reply)
            
            return {
                "reply": reply,
                "updated_context": context_dict,
                "is_recommendation": False
            }
        else:
            print("✅ Context Sufficient. Triggering RAG & Reasoning...")
            recommendation_dict = generate_recommendation(user_message, session.context)

            formatted_reply = f"🌱 **Recommendation:** {recommendation_dict.get('recommendation', '')}\n\n"
            formatted_reply += f"🔬 **Why it works:** {recommendation_dict.get('why_it_works', '')}\n\n"
            
            impacted = recommendation_dict.get('impacted_metrics', [])
            formatted_reply += f"📊 **Impacted Metrics:** {', '.join(impacted) if isinstance(impacted, list) else impacted}\n\n"
            
            formatted_reply += f"⏱ **Time Horizon:** {recommendation_dict.get('time_horizon', '')}\n\n"
            
            sources = recommendation_dict.get('resolved_sources', [])
            if sources:
                formatted_reply += "📚 **Evidence & Authoritative Sources:**\n"
                for src in sources:
                    formatted_reply += f"- **{src.get('organization')}**: *{src.get('title')}* ([Link]({src.get('url')}))\n"
            else:
                formatted_reply += "📚 **Evidence:** Derived from general environmental scientific guidelines."

            session.add_message("assistant", formatted_reply)

            return {
                "reply": formatted_reply,
                "updated_context": context_dict,
                "is_recommendation": True
            }

# Singleton instance
conversation_manager = ConversationManager()

if __name__ == "__main__":
    print("--- Simulating Real Conversation Flow ---")
    mgr = ConversationManager()
    test_session_id = "user_akshat_001"
    
    print("\n🗣️ USER (Turn 1): 'Biodiversity is declining on my land. What should I do?'")
    res1 = mgr.process_turn(test_session_id, "Biodiversity is declining on my land. What should I do?")
    print(f"\n🤖 AI RESPONSE (Turn 1):\n{res1['reply']}")
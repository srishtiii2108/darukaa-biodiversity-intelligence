from memory_manager import memory_manager
from context_extractor import extract_environmental_data
from context_validator import validate_context
from reasoning_engine import generate_recommendation
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

        # 4. Validate Context (Check if we have at least 3 variables)
        context_dict = session.context.model_dump()
        validation_result = validate_context(context_dict)

        # 5. Branch Logic: Clarification vs Recommendation
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
            # Trigger our AI Scientist Pipeline
            recommendation_dict = generate_recommendation(user_message, session.context)

            # Format the final response for the user
            formatted_reply = f"🌱 **Recommendation:** {recommendation_dict.get('recommendation', '')}\n\n"
            formatted_reply += f"🔬 **Why it works:** {recommendation_dict.get('why_it_works', '')}\n\n"
            
            impacted = recommendation_dict.get('impacted_metrics', [])
            formatted_reply += f"📊 **Impacted Metrics:** {', '.join(impacted) if isinstance(impacted, list) else impacted}\n\n"
            
            formatted_reply += f"⏱ **Time Horizon:** {recommendation_dict.get('time_horizon', '')}\n\n"
            
            # Format Traceable Evidence Sources cleanly
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
    # Let's simulate a real multi-turn conversation
    print("--- Simulating Real Conversation Flow ---")
    mgr = ConversationManager()
    test_session_id = "user_akshat_001"
    
    print("\n🗣️ USER (Turn 1): 'Biodiversity is declining on my land. What should I do?'")
    res1 = mgr.process_turn(test_session_id, "Biodiversity is declining on my land. What should I do?")
    print(f"\n🤖 AI RESPONSE (Turn 1):\n{res1['reply']}")
    
    print("\n--------------------------------------------------")
    print("🗣️ USER (Turn 2): 'My rainfall is low, I grow monoculture wheat, and soil carbon is 0.3%'")
    res2 = mgr.process_turn(test_session_id, "My rainfall is low, I grow monoculture wheat, and soil carbon is 0.3%")
    print(f"\n🤖 AI RESPONSE (Turn 2):\n{res2['reply']}")
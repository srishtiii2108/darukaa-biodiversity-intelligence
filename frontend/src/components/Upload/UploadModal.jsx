import { useState, useRef } from 'react';
import { X, UploadCloud, FileText, CheckCircle2, Loader2, AlertCircle } from 'lucide-react';
import { uploadScientificDocument } from '../../services/api';

export default function UploadModal({ isOpen, onClose, sessionId, onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('idle');
  const [errorMessage, setErrorMessage] = useState('');
  const fileInputRef = useRef(null);

  if (!isOpen) return null;

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setStatus('idle');
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setStatus('uploading');
    setErrorMessage('');

    try {
      await uploadScientificDocument(file, sessionId);
      setStatus('success');
      if (onUploadSuccess) {
        onUploadSuccess(file.name);
      }
      setTimeout(() => {
        setFile(null);
        setStatus('idle');
        onClose();
      }, 1500);
    } catch (error) {
      console.error("[UploadModal] Error:", error);
      setStatus('error');
      setErrorMessage(error.message || 'Failed to ingest document.');
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-darukaa-text/20 backdrop-blur-sm p-4">
      <div className="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden border border-darukaa-border">
        <div className="flex items-center justify-between px-6 py-4 border-b border-darukaa-border bg-[#FAFCFB]">
          <h3 className="font-serif font-bold text-lg text-darukaa-text">Add to Knowledge Base</h3>
          <button onClick={onClose} className="text-darukaa-muted hover:text-darukaa-text">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-6">
          {!file ? (
            <div 
              onClick={() => fileInputRef.current?.click()}
              className="border-2 border-dashed border-darukaa-border rounded-xl p-8 flex flex-col items-center justify-center text-center cursor-pointer hover:border-darukaa-green/50 hover:bg-[#F4F9F5] transition-all"
            >
              <div className="w-12 h-12 bg-[#E8F0EA] text-darukaa-green rounded-full flex items-center justify-center mb-4">
                <UploadCloud className="w-6 h-6" />
              </div>
              <p className="text-sm font-medium text-darukaa-text mb-1">Click to upload scientific document</p>
              <p className="text-xs text-darukaa-muted">Supports .txt, .pdf (Max 5MB)</p>
              <input 
                type="file" 
                ref={fileInputRef} 
                onChange={handleFileChange} 
                className="hidden" 
                accept=".txt,.pdf"
              />
            </div>
          ) : (
            <div className="border border-darukaa-border rounded-xl p-4 flex items-center justify-between bg-[#FAFCFB]">
              <div className="flex items-center gap-3 overflow-hidden">
                <FileText className="w-8 h-8 text-darukaa-green shrink-0" />
                <div className="truncate">
                  <p className="text-sm font-medium text-darukaa-text truncate">{file.name}</p>
                  <p className="text-xs text-darukaa-muted">{(file.size / 1024).toFixed(1)} KB</p>
                </div>
              </div>
              <button onClick={() => setFile(null)} className="text-darukaa-muted hover:text-red-500 p-2">
                <X className="w-4 h-4" />
              </button>
            </div>
          )}

          {status === 'error' && (
            <div className="mt-4 p-3 bg-red-50 border border-red-100 rounded-lg flex items-center gap-2 text-red-600 text-xs font-medium">
              <AlertCircle className="w-4 h-4 shrink-0" /> {errorMessage}
            </div>
          )}
          {status === 'success' && (
            <div className="mt-4 p-3 bg-[#E8F0EA] border border-darukaa-green/20 rounded-lg flex items-center gap-2 text-darukaa-green text-xs font-medium">
              <CheckCircle2 className="w-4 h-4 shrink-0" /> Document ingested and vectorized successfully!
            </div>
          )}
        </div>

        <div className="px-6 py-4 border-t border-darukaa-border bg-[#FAFCFB] flex justify-end gap-3">
          <button onClick={onClose} className="px-4 py-2 text-sm font-medium text-darukaa-text hover:bg-gray-100 rounded-full">
            Cancel
          </button>
          <button 
            onClick={handleUpload}
            disabled={!file || status === 'uploading' || status === 'success'}
            className="bg-darukaa-green text-white px-5 py-2 rounded-full text-sm font-medium flex items-center gap-2 hover:bg-opacity-90 disabled:opacity-50"
          >
            {status === 'uploading' ? <><Loader2 className="w-4 h-4 animate-spin" /> Ingesting...</> : 'Upload to RAG'}
          </button>
        </div>
      </div>
    </div>
  );
}
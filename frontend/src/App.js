import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  Music, Radio, Zap, Scale, Target, Sparkles, 
  Play, Download, Settings, Info, Github, ExternalLink,
  Clock, Gauge, Sliders, Volume2, HardDrive, CheckCircle,
  XCircle, Loader, ChevronDown, ChevronUp, Package
} from 'lucide-react';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const EXAMPLES = {
  musicgen: [
    "Upbeat electronic dance music with heavy bass and synth melodies",
    "Calm acoustic guitar with soft piano accompaniment",
    "Epic orchestral soundtrack with dramatic strings and brass",
    "Lo-fi hip hop beat with vinyl crackle and mellow piano",
    "Energetic rock song with electric guitar and heavy drums"
  ],
  audiogen: [
    "Sound of rain falling on a window with distant thunder",
    "Busy city street with cars passing and people talking",
    "Forest ambience with birds chirping and leaves rustling",
    "Ocean waves crashing on a beach with seagulls",
    "Dog barking in a park with birds chirping"
  ]
};

function App() {
  const [modelType, setModelType] = useState('musicgen');
  const [modelSize, setModelSize] = useState('medium');
  const [prompt, setPrompt] = useState('');
  const [duration, setDuration] = useState(10);
  const [temperature, setTemperature] = useState(1.0);
  const [topK, setTopK] = useState(250);
  const [cfgCoef, setCfgCoef] = useState(4.5);
  const [showAdvanced, setShowAdvanced] = useState(false);
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  // Model management state
  const [showModelManager, setShowModelManager] = useState(false);
  const [modelStatus, setModelStatus] = useState({});
  const [downloadingModel, setDownloadingModel] = useState(null);
  const [loadingModel, setLoadingModel] = useState(null);

  const MODEL_SIZES = {
    small: { name: 'Fast', quality: '60-70%', speed: 'Fast', icon: Zap, desc: 'Quick generation' },
    medium: { name: 'Balanced', quality: '75-85%', speed: 'Medium', icon: Scale, desc: 'Best for most uses' },
    large: { name: 'Premium', quality: '90-95%', speed: 'Slow', icon: Target, desc: 'Highest quality' }
  };

  // Fetch model status on mount
  useEffect(() => {
    fetchModelStatus();
  }, []);

  const fetchModelStatus = async () => {
    try {
      const response = await axios.get(`${API_URL}/models/status`);
      setModelStatus(response.data);
    } catch (err) {
      console.error('Failed to fetch model status:', err);
    }
  };

  const handleDownloadModel = async (size) => {
    setDownloadingModel(size);
    try {
      await axios.post(`${API_URL}/models/download/${size}`);
      await fetchModelStatus();
      alert(`Model ${size} downloaded successfully!`);
    } catch (err) {
      alert(`Failed to download model: ${err.response?.data?.detail || err.message}`);
    } finally {
      setDownloadingModel(null);
    }
  };

  const handleLoadModel = async (size) => {
    setLoadingModel(size);
    try {
      await axios.post(`${API_URL}/models/load/${size}`);
      await fetchModelStatus();
    } catch (err) {
      alert(`Failed to load model: ${err.response?.data?.detail || err.message}`);
    } finally {
      setLoadingModel(null);
    }
  };

  const handleUnloadModel = async (size) => {
    try {
      await axios.post(`${API_URL}/models/unload/${size}`);
      await fetchModelStatus();
    } catch (err) {
      alert(`Failed to unload model: ${err.response?.data?.detail || err.message}`);
    }
  };

  const handleGenerate = async () => {
    if (!prompt.trim()) {
      setError('Please enter a prompt');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post(`${API_URL}/generate`, {
        prompt: prompt.trim(),
        duration: parseFloat(duration),
        model_type: modelType,
        model_size: modelSize,
        temperature: parseFloat(temperature),
        top_k: parseInt(topK),
        cfg_coef: parseFloat(cfgCoef)
      });

      setResult({
        audioUrl: `${API_URL}${response.data.audio_url}`,
        filename: response.data.filename,
        duration: response.data.duration,
        modelUsed: response.data.model_used
      });
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to generate audio. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleExampleClick = (examplePrompt) => {
    setPrompt(examplePrompt);
  };

  return (
    <div className="App">
      {/* Header */}
      <header className="header">
        <div className="header-content">
          <div className="logo-section">
            <div className="logo">
              <Music className="logo-icon" />
              <span className="logo-text">AI Music Studio Lite</span>
            </div>
            <span className="version-badge">v3.0 Open Source</span>
          </div>
          <a 
            href="https://github.com/facebookresearch/audiocraft" 
            target="_blank" 
            rel="noopener noreferrer"
            className="github-link"
          >
            <Github size={20} />
            <span>Meta AudioCraft</span>
          </a>
        </div>
      </header>

      {/* Hero Section */}
      <div className="hero">
        <div className="hero-badge">
          <Sparkles size={16} />
          <span>Powered by Meta's AudioCraft Models</span>
        </div>
        <h1 className="hero-title">
          The new standard for <span className="gradient-text">AI Music Generation</span>
        </h1>
        <p className="hero-subtitle">
          Produce studio-quality tracks in seconds. A professional-grade experience powered by next-gen audio models.
        </p>
        <div className="hero-credits">
          <p>
            <strong>Built with:</strong> Meta's AudioCraft (MusicGen & AudioGen) • 
            <a href="https://github.com/facebookresearch/audiocraft" target="_blank" rel="noopener noreferrer">
              <ExternalLink size={14} /> View on GitHub
            </a>
          </p>
          <p className="lite-version">
            <Info size={14} />
            <span>
              <strong>AI Music Studio(AIMusicStudio.pro)</strong> presents this lite version for instant local use - 
              Free, unlimited, and runs on CPU with no setup headache!
            </span>
          </p>
        </div>
      </div>

      {/* Main Container - Single Unified Card */}
      <div className="container">
        {/* Model Manager Section */}
        <div className="model-manager-card">
          <button 
            className="model-manager-toggle"
            onClick={() => setShowModelManager(!showModelManager)}
          >
            <Package size={18} />
            <span>Model Manager</span>
            <span className="model-manager-hint">
              Download only the models you need
            </span>
            {showModelManager ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
          </button>

          {showModelManager && (
            <div className="model-manager-content">
              <div className="model-manager-info">
                <Info size={16} />
                <p>
                  Models are downloaded on-demand. Download only what you need to save disk space.
                  First-time download may take 5-15 minutes depending on your internet speed.
                </p>
              </div>

              <div className="models-grid">
                {Object.entries(MODEL_SIZES).map(([size, info]) => {
                  const status = modelStatus[size] || {};
                  const isDownloaded = status.downloaded;
                  const isLoaded = status.loaded;
                  const isDownloading = downloadingModel === size;
                  const isLoadingNow = loadingModel === size;

                  return (
                    <div key={size} className="model-card">
                      <div className="model-card-header">
                        <div className="model-card-title">
                          <info.icon size={20} />
                          <div>
                            <h4>{info.name}</h4>
                            <p className="model-card-subtitle">{status.params || 'N/A'} • {status.size_gb || '~2-6GB'}</p>
                          </div>
                        </div>
                        <div className="model-status-badges">
                          {isLoaded && (
                            <span className="status-badge loaded">
                              <CheckCircle size={12} />
                              Loaded
                            </span>
                          )}
                          {isDownloaded && !isLoaded && (
                            <span className="status-badge downloaded">
                              <HardDrive size={12} />
                              Downloaded
                            </span>
                          )}
                          {!isDownloaded && (
                            <span className="status-badge not-downloaded">
                              <XCircle size={12} />
                              Not Downloaded
                            </span>
                          )}
                        </div>
                      </div>

                      <div className="model-card-info">
                        <div className="model-info-row">
                          <span>Quality:</span>
                          <strong>{info.quality}</strong>
                        </div>
                        <div className="model-info-row">
                          <span>Speed:</span>
                          <strong>{info.speed}</strong>
                        </div>
                        <p className="model-description">{info.desc}</p>
                      </div>

                      <div className="model-card-actions">
                        {!isDownloaded && (
                          <button
                            className="model-action-btn primary"
                            onClick={() => handleDownloadModel(size)}
                            disabled={isDownloading}
                          >
                            {isDownloading ? (
                              <>
                                <Loader size={14} className="spin" />
                                Downloading...
                              </>
                            ) : (
                              <>
                                <Download size={14} />
                                Download
                              </>
                            )}
                          </button>
                        )}
                        {isDownloaded && !isLoaded && (
                          <button
                            className="model-action-btn secondary"
                            onClick={() => handleLoadModel(size)}
                            disabled={isLoadingNow}
                          >
                            {isLoadingNow ? (
                              <>
                                <Loader size={14} className="spin" />
                                Loading...
                              </>
                            ) : (
                              <>
                                <Play size={14} />
                                Load into Memory
                              </>
                            )}
                          </button>
                        )}
                        {isLoaded && (
                          <button
                            className="model-action-btn danger"
                            onClick={() => handleUnloadModel(size)}
                          >
                            <XCircle size={14} />
                            Unload
                          </button>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>

              <div className="model-manager-footer">
                <p>
                  <strong>Tip:</strong> You can download all models or just one. 
                  Models are cached and won't be re-downloaded. 
                  Total space needed: ~2GB (small), ~4GB (medium), ~6GB (large).
                </p>
              </div>
            </div>
          )}
        </div>

        <div className="main-card">
          {/* Generation Mode & Quality in one row */}
          <div className="control-row">
            <div className="control-section">
              <h3 className="control-label">
                <Radio size={18} />
                Generation Mode
              </h3>
              <div className="mode-buttons">
                <button
                  className={`mode-btn ${modelType === 'musicgen' ? 'active' : ''}`}
                  onClick={() => setModelType('musicgen')}
                >
                  <Music size={20} />
                  <div>
                    <div className="mode-title">MusicGen</div>
                    <div className="mode-desc">Full compositions</div>
                  </div>
                </button>
                <button
                  className={`mode-btn ${modelType === 'audiogen' ? 'active' : ''}`}
                  onClick={() => setModelType('audiogen')}
                >
                  <Volume2 size={20} />
                  <div>
                    <div className="mode-title">AudioGen</div>
                    <div className="mode-desc">Sound effects</div>
                  </div>
                </button>
              </div>
            </div>

            <div className="control-section">
              <h3 className="control-label">
                <Gauge size={18} />
                Quality Level (Model)
              </h3>
              <div className="quality-buttons">
                {Object.entries(MODEL_SIZES).map(([size, info]) => {
                  const IconComponent = info.icon;
                  return (
                    <button
                      key={size}
                      className={`quality-btn ${modelSize === size ? 'active' : ''}`}
                      onClick={() => setModelSize(size)}
                      title={`${info.quality} quality, ${info.speed} speed`}
                    >
                      <IconComponent size={18} />
                      <div>
                        <div className="quality-title">{info.name}</div>
                        <div className="quality-stats">{info.quality}</div>
                      </div>
                    </button>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Prompt Section */}
          <div className="prompt-section">
            <h3 className="control-label">
              <Sparkles size={18} />
              Describe Your {modelType === 'musicgen' ? 'Music' : 'Sound'}
            </h3>
            <textarea
              className="prompt-input"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder={`e.g., "${EXAMPLES[modelType][0]}"`}
              rows={3}
            />
          </div>

          {/* Settings Section */}
          <div className="settings-section">
            <div className="settings-header">
              <h3 className="control-label">
                <Sliders size={18} />
                Settings
              </h3>
              <button 
                className="advanced-toggle"
                onClick={() => setShowAdvanced(!showAdvanced)}
              >
                <Settings size={14} />
                {showAdvanced ? 'Hide' : 'Show'} Advanced
              </button>
            </div>
            
            <div className="settings-content">
              <div className="setting-row">
                <label>
                  <Clock size={14} />
                  Duration
                </label>
                <div className="slider-group">
                  <input
                    type="range"
                    min="1"
                    max="300"
                    value={duration}
                    onChange={(e) => setDuration(e.target.value)}
                    className="slider"
                  />
                  <span className="value">{duration}s</span>
                </div>
              </div>

              {showAdvanced && (
                <>
                  <div className="setting-row">
                    <label>Temperature</label>
                    <div className="slider-group">
                      <input
                        type="range"
                        min="0.1"
                        max="2.0"
                        step="0.1"
                        value={temperature}
                        onChange={(e) => setTemperature(e.target.value)}
                        className="slider"
                      />
                      <span className="value">{temperature}</span>
                    </div>
                  </div>
                  <div className="setting-row">
                    <label>Top-K</label>
                    <div className="slider-group">
                      <input
                        type="range"
                        min="0"
                        max="500"
                        value={topK}
                        onChange={(e) => setTopK(e.target.value)}
                        className="slider"
                      />
                      <span className="value">{topK}</span>
                    </div>
                  </div>
                  <div className="setting-row">
                    <label>CFG Scale</label>
                    <div className="slider-group">
                      <input
                        type="range"
                        min="1"
                        max="10"
                        step="0.5"
                        value={cfgCoef}
                        onChange={(e) => setCfgCoef(e.target.value)}
                        className="slider"
                      />
                      <span className="value">{cfgCoef}</span>
                    </div>
                  </div>
                </>
              )}
            </div>
          </div>

          {/* Generate Button */}
          <button
            className="generate-btn"
            onClick={handleGenerate}
            disabled={loading || !prompt.trim()}
          >
            {loading ? (
              <>
                <div className="spinner" />
                Generating...
              </>
            ) : (
              <>
                <Sparkles size={18} />
                Generate Audio
              </>
            )}
          </button>

          {/* Loading State */}
          {loading && (
            <div className="status-card loading">
              <div className="wave-animation">
                <div className="wave"></div>
                <div className="wave"></div>
                <div className="wave"></div>
              </div>
              <p>Creating with {MODEL_SIZES[modelSize].name} quality...</p>
              <p className="hint">~{modelSize === 'small' ? '15-20' : modelSize === 'medium' ? '30-40' : '60-90'}s</p>
            </div>
          )}

          {/* Error State */}
          {error && (
            <div className="status-card error">
              <Info size={18} />
              <div>
                <strong>Error</strong>
                <p>{error}</p>
              </div>
            </div>
          )}

          {/* Result */}
          {result && (
            <div className="status-card success">
              <div className="result-header">
                <h4>
                  <Play size={18} />
                  Generated Audio
                </h4>
                <a 
                  href={result.audioUrl} 
                  download={result.filename}
                  className="download-btn"
                >
                  <Download size={14} />
                  Download
                </a>
              </div>
              <audio
                className="audio-player"
                controls
                src={result.audioUrl}
              />
              <div className="result-meta">
                <span><Clock size={12} /> {result.duration}s</span>
                <span><Gauge size={12} /> {MODEL_SIZES[modelSize].name}</span>
                <span><Radio size={12} /> {result.modelUsed}</span>
              </div>
            </div>
          )}

          {/* Example Prompts */}
          <div className="examples-section">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
              <h3 className="control-label">
                <Sparkles size={18} />
                Example Prompts
              </h3>
              <button
                className="open-files-btn"
                title="View all your generated audio files in Windows Explorer"
                onClick={() => {
                  alert('To view your files:\n\n1. Look for "OPEN_MY_AUDIO_FILES.bat" in the app folder\n2. Double-click it to open the outputs folder\n\nOr find files in: backend/outputs/');
                }}
              >
                <ExternalLink size={14} />
                My Files
              </button>
            </div>
            <div className="examples-list">
              {EXAMPLES[modelType].map((example, index) => (
                <button
                  key={index}
                  className="example-item"
                  onClick={() => handleExampleClick(example)}
                >
                  {example}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <div className="footer-section">
            <h4>Credits & Attribution</h4>
            <p>
              Powered by <strong>Meta's AudioCraft</strong> - Open source models for audio generation
            </p>
            <a href="https://github.com/facebookresearch/audiocraft" target="_blank" rel="noopener noreferrer">
              <Github size={16} />
              facebook/audiocraft
            </a>
          </div>
          <div className="footer-section">
            <h4>About This Version</h4>
            <p>
              <strong>AIMusicStudio.pro</strong> presents this lite version for the community.
              Free, unlimited, runs locally on your CPU - no setup headache!
            </p>
          </div>
          <div className="footer-section">
            <h4>License</h4>
            <p>MIT License - Free & Open Source</p>
            <p className="footer-note">
              Models: Meta AudioCraft (MIT) • Interface: AI Music Studio Lite (MIT)
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;

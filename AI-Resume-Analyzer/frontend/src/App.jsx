import { useState } from "react";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeResume = async () => {
    if (!resume) {
      setError("Please upload your resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          body: formData
        }
      );

      if (!response.ok) {
        throw new Error("Analysis failed.");
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setError(
        "Could not connect to the backend. Make sure FastAPI is running."
      );
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="glow glow-one"></div>
      <div className="glow glow-two"></div>

      <header className="navbar">
        <div className="brand">
          <div className="brand-icon">AI</div>
          <div>
            <div className="brand-name">
              Resume<span>IQ</span>
            </div>
            <div className="brand-subtitle">
              AI Career Intelligence
            </div>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI Engine Online
        </div>
      </header>

      <main className="container">
        <section className="hero">
          <div className="hero-badge">
            ✦ INTELLIGENT RESUME ANALYSIS
          </div>

          <h1>
            Know how well your resume
            <span> matches the job.</span>
          </h1>

          <p>
            Analyze your resume against any job description,
            discover missing skills, and get actionable
            recommendations.
          </p>
        </section>

        <section className="workspace">
          <div className="input-card">
            <div className="section-number">01</div>

            <div className="section-heading">
              <h2>Upload your resume</h2>
              <p>PDF format recommended</p>
            </div>

            <label className="upload-box">
              <input
                type="file"
                accept=".pdf"
                onChange={(event) =>
                  setResume(event.target.files[0])
                }
              />

              <div className="upload-icon">↑</div>

              <div className="upload-title">
                {resume ? resume.name : "Drop your resume here"}
              </div>

              <div className="upload-description">
                {resume
                  ? "Resume selected successfully"
                  : "or click to browse your files"}
              </div>

              <div className="upload-format">
                PDF • MAX 10MB
              </div>
            </label>
          </div>

          <div className="input-card">
            <div className="section-number">02</div>

            <div className="section-heading">
              <h2>Job description</h2>
              <p>Paste the position you're applying for</p>
            </div>

            <textarea
              className="job-input"
              placeholder="Paste the complete job description here..."
              value={jobDescription}
              onChange={(event) =>
                setJobDescription(event.target.value)
              }
            />

            <div className="character-count">
              {jobDescription.length} characters
            </div>
          </div>
        </section>

        <button
          className="analyze-button"
          onClick={analyzeResume}
          disabled={loading}
        >
          <span>
            {loading ? "Analyzing your profile..." : "Analyze Resume"}
          </span>

          {!loading && (
            <span className="button-arrow">→</span>
          )}
        </button>

        {error && (
          <div className="error">
            <span>!</span>
            {error}
          </div>
        )}

        {result && (
          <section className="results">
            <div className="results-header">
              <div>
                <div className="hero-badge">
                  ✦ ANALYSIS COMPLETE
                </div>

                <h2>Your Match Report</h2>

                <p>
                  Here's how your profile aligns with this position.
                </p>
              </div>
            </div>

            <div className="score-panel">
              <div className="score-circle">
                <div className="score-number">
                  {result.analysis.overall_score}
                  <span>%</span>
                </div>
                <div className="score-label">MATCH</div>
              </div>

              <div className="score-details">
                <div className="metric">
                  <span>Skill Match</span>
                  <strong>
                    {result.analysis.skill_match_score}%
                  </strong>
                </div>

                <div className="metric">
                  <span>Required Skills</span>
                  <strong>
                    {result.analysis.required_skill_score}%
                  </strong>
                </div>

                <div className="metric">
                  <span>Preferred Skills</span>
                  <strong>
                    {result.analysis.preferred_skill_score}%
                  </strong>
                </div>

                <div className="metric">
                  <span>Text Similarity</span>
                  <strong>
                    {result.analysis.text_similarity_score}%
                  </strong>
                </div>
              </div>
            </div>

            <div className="result-grid">
              <div className="result-card">
                <div className="result-card-title">
                  <span className="green-dot"></span>
                  Matched Required Skills
                </div>

                <div className="skills">
                  {result.analysis.matched_required.length > 0 ? (
                    result.analysis.matched_required.map((skill) => (
                      <span
                        className="skill matched"
                        key={skill}
                      >
                        ✓ {skill}
                      </span>
                    ))
                  ) : (
                    <span className="empty-text">
                      No required skills matched.
                    </span>
                  )}
                </div>
              </div>

              <div className="result-card">
                <div className="result-card-title">
                  <span className="red-dot"></span>
                  Missing Required Skills
                </div>

                <div className="skills">
                  {result.analysis.missing_required.length > 0 ? (
                    result.analysis.missing_required.map((skill) => (
                      <span
                        className="skill missing"
                        key={skill}
                      >
                        + {skill}
                      </span>
                    ))
                  ) : (
                    <span className="empty-text">
                      No required skills missing.
                    </span>
                  )}
                </div>
              </div>

              <div className="result-card">
                <div className="result-card-title">
                  <span className="green-dot"></span>
                  Matched Preferred Skills
                </div>

                <div className="skills">
                  {result.analysis.matched_preferred.length > 0 ? (
                    result.analysis.matched_preferred.map((skill) => (
                      <span
                        className="skill matched"
                        key={skill}
                      >
                        ✓ {skill}
                      </span>
                    ))
                  ) : (
                    <span className="empty-text">
                      No preferred skills matched.
                    </span>
                  )}
                </div>
              </div>

              <div className="result-card">
                <div className="result-card-title">
                  <span className="red-dot"></span>
                  Missing Preferred Skills
                </div>

                <div className="skills">
                  {result.analysis.missing_preferred.length > 0 ? (
                    result.analysis.missing_preferred.map((skill) => (
                      <span
                        className="skill missing"
                        key={skill}
                      >
                        + {skill}
                      </span>
                    ))
                  ) : (
                    <span className="empty-text">
                      No preferred skills missing.
                    </span>
                  )}
                </div>
              </div>
            </div>

            <div className="recommendations">
              <div className="result-card-title">
                <span className="purple-dot"></span>
                Recommended Next Steps
              </div>

              {result.recommendations.map((item, index) => (
                <div
                  className="recommendation"
                  key={index}
                >
                  <div className="recommendation-number">
                    {String(index + 1).padStart(2, "0")}
                  </div>

                  <div>
                    <strong>{item.skill}</strong>
                    <p>{item.recommendation}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}
      </main>

      <footer>
        Built with React • FastAPI • Python • NLP
      </footer>
    </div>
  );
}

export default App;

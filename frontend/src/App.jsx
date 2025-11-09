import { useState } from "react";
import "./App.css";

const ideaTemplates = [
  {
    title: "Trend Remix: {keyword} Glow-Up",
    hook: "Flip the latest foodie trend on its head with a {toneLower} spin that hooks scrollers in the first three seconds.",
    concept:
      "Start with a quick shot of the finished dish. Cut to a behind-the-scenes montage of how you discovered this idea, then reveal the secret ingredient or twist that makes it pop.",
    callToAction:
      "Ask viewers which creative twist they want to see next or invite them to duet with their version.",
    feature: "Include a text overlay that pins the main tip at the top of the screen.",
  },
  {
    title: "Street-Style Spotlight: {keyword}",
    hook: "Take your audience on a street food adventure that feels immersive and fast-paced.",
    concept:
      "Shoot handheld footage while narrating the origin of the dish. Use jump cuts for each step, ending with a slow-motion taste test and your honest reaction.",
    callToAction:
      "Prompt viewers to drop their favorite hidden gem spots using a branded hashtag.",
    feature: "Add ambient street sounds beneath upbeat music to layer the vibe.",
  },
  {
    title: "Rapid-Fire Recipe: {keyword} in 60 Seconds",
    hook: "Deliver a power-packed mini masterclass with crisp cuts and on-screen timers.",
    concept:
      "Open with ingredients laid out, then speed-run through each step with punchy captions. Wrap up with plating tips and a satisfying close-up bite.",
    callToAction: "Challenge viewers to recreate it and stitch their results.",
    feature: "Use split screens to compare 'expectation vs. your twist.'",
  },
  {
    title: "Behind the Scenes: Building the {keyword} Hook",
    hook: "Show your creative process to humanize your brand and build trust.",
    concept:
      "Start with mood board snapshots, then share quick clips of recipe testing bloopers and final success. Layer commentary or captions for storytelling.",
    callToAction: "Invite your community to vote on your next experiment.",
    feature: "Overlay handwritten notes or sketches as animated stickers.",
  },
  {
    title: "Community Collab: {keyword} Fan Challenge",
    hook: "Turn your audience into co-creators with an accessible challenge.",
    concept:
      "Announce the challenge rules, show your version, then highlight stitched responses or predictions of what followers will submit.",
    callToAction: "Encourage users to tag you and use the featured challenge hashtag.",
    feature: "Pin a comment with top submissions to keep engagement rolling.",
  },
];

const generateCreativePlan = ({ prompt, platform, tone, videoLength }) => {
  const toneLower = tone.toLowerCase();

  const selectedIdeas = [...ideaTemplates]
    .sort(() => Math.random() - 0.5)
    .slice(0, 3)
    .map((template, index) => ({
      id: `${template.title}-${index}`,
      description: `${template.hook.replace("{toneLower}", toneLower)} ${template.concept}`,
    }));

  return {
    trendIdeas: selectedIdeas,
  };
};

const DEFAULT_PLATFORM = "TikTok";
const DEFAULT_TONE = "High energy";
const DEFAULT_LENGTH = 60;

function App() {
  const [prompt, setPrompt] = useState("");
  const [creativePlan, setCreativePlan] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    setError("");

    if (!prompt.trim()) {
      setError("Tell us what you want to create so we can ideate with you.");
      return;
    }

    setIsLoading(true);

    setTimeout(() => {
      const plan = generateCreativePlan({
        prompt,
        platform: DEFAULT_PLATFORM,
        tone: DEFAULT_TONE,
        videoLength: DEFAULT_LENGTH,
      });
      setCreativePlan(plan);
      setIsLoading(false);
    }, 400);
  };

  return (
    <div className="page">
      <header className="hero">
        <div>
          <p className="eyebrow">FoodTok Creative Lab</p>
          <h1>Unlock your next viral food video concept</h1>
          <p className="subtitle">
            Describe what you want to film and get platform-ready hooks, story beats,
            and trending angles in seconds.
          </p>
        </div>
        <div className="hero-badge">
          <span className="hero-badge__emoji" role="img" aria-label="sparkles">
            ✨
          </span>
          <div>
            <p className="hero-badge__title">Built for food influencers</p>
            <p className="hero-badge__meta">Trends refresh daily</p>
          </div>
        </div>
      </header>

      <main className="content">
        <section className="prompt-card">
          <form onSubmit={handleSubmit} className="prompt-form">
            <label htmlFor="prompt" className="field-label">
              What do you want to make next?
            </label>
            <textarea
              id="prompt"
              placeholder="e.g. Explore viral fall dessert ideas with seasonal ingredients and cozy vibes."
              value={prompt}
              onChange={(event) => setPrompt(event.target.value)}
              rows={5}
              className="field-input"
            />

            {error && <p className="form-error">{error}</p>}

            <button type="submit" className="generate-button" disabled={isLoading}>
              {isLoading ? "Curating ideas..." : "Generate my video plan"}
            </button>
          </form>
        </section>

        <section className="results">
          {!creativePlan && !isLoading && (
            <div className="empty-state">
              <p className="empty-title">Ideas appear here</p>
              <p className="empty-body">
                Share your concept above to see platform-ready hooks, formats, and trend inspiration.
              </p>
            </div>
          )}

          {isLoading && (
            <div className="loading-state">
              <span className="loading-spinner" aria-hidden /> Fetching trends and remixing ideas...
            </div>
          )}

          {creativePlan && !isLoading && (
            <div className="plan">
              <div className="plan-header">
                <h2>Trend Ideas</h2>
              </div>

              <div className="ideas">
                <h3>Video concepts</h3>
                <div className="idea-grid">
                  {creativePlan.trendIdeas.map((idea) => (
                    <article key={idea.id} className="idea-card">
                      <p className="idea-hook">{idea.description}</p>
                    </article>
                  ))}
                </div>
              </div>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;

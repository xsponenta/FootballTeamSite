import '../styles.css';
import background from '../with_fans.jpg'

const Main = () => {
    return (
        <main className="main">
            <div className="header-image">
                <img src={background} alt="Heading Image" />
                <h1>Petro United with Fans!</h1>
            </div>

            {/* Videos component */}
            <div className="videos">
                {/* Tabs */}
                <div className="tabs">
                    <button>Tournament</button>
                    <button>Clips</button>
                    <button>Episodes</button>
                    <button>Interviews</button>
                </div>
                {/* Videos content */}
                <div className="content">
                    {/* Individual video components */}
                    {Array.from({ length: 6 }, (_, i) => (
                        <div key={i} className="video">Subtitle</div>
                    ))}
                </div>
            </div>
            {/* Last Match component */}
            <div className="last-match">
                <div className="controls">
                    <button>Match Item</button>
                    <button>Statistics</button>
                    <button>Highlights</button>
                </div>
                <div className="scoreboard">
                    <div>
                        <h2>Petro United</h2>
                        <p>Player - Goal Time</p>
                        <p>Player - Goal Time</p>
                    </div>
                    <div>
                        <h2>League</h2>
                        <div className="score">Score</div>
                        <button>Watch Preview</button>
                    </div>
                    <div>
                        <h2>Enemy team</h2>
                        <p>Player - Goal Time</p>
                        <p>Player - Goal Time</p>
                    </div>
                </div>
            </div>
        </main>
    );
};

export default Main;
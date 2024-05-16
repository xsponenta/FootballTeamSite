import '../styles.css';
import background from '../with_fans.jpg'

const Main = () => {
    return (
        <main className="main">
            <div className="header-image">
                <img src={background} alt="Heading Image" />
                <h1>Petro United with Fans!</h1>
            </div>

            <div className="videos">
                <h3>Videos by Petro United</h3>
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
                    <h3>Last match review</h3>
                    <button>Highlights</button>
                </div>
                <div className="scoreboard">
                    <div className='league'>
                        <h2>League</h2>
                    </div>
                    <div className="score">
                        <h2>Petro United</h2>
                        <h2>Score</h2>
                        <h2>Enemy team</h2>
                    </div>
                </div>
                <button>Watch Preview</button>
                <img src="preview.png"></img>
            </div>
        </main>
    );
};

export default Main;
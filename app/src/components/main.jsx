import '../styles.css';
import background from '../with_fans.jpg'
import logo from '../logo.png'
import enemy from '../enemy.png'

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
                        <div key={i} className="video"></div>
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
                        <img className="our" width="5%" src={logo}></img>
                        <h2>Petro United</h2>
                        <h2>Score</h2>
                        <h2>Enemy team</h2>
                        <img className="enemy" width="11%" src={enemy}></img>
                    </div>
                    <div className="preview-button">
                        <button>Watch Preview</button>
                    </div>
                </div>
            </div>
        </main>
    );
};

export default Main;
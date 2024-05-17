import '../styles.css';
import background from '../with_fans.jpg'
import logo from '../logo.png'
import enemy from '../enemy.png'
import React, { useState, useEffect } from 'react';

const Main = () => {
    const [jsonData, setData] = useState(null);
    useEffect(() => {
      fetchData();
    }, []);
  
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/get_recent_highlights');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const jsonData = await response.json();
        console.log(jsonData);
        console.log("GAY")
        setData(jsonData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    return (
        <main className="main">
            {jsonData ? (
                <div>
            <div className="header-image">
                <img src={background} alt="Heading Image" />
                <h1>Petro United with Fans!</h1>
            </div>

            <div className="videos">
                {/* Individual video components */}
                {jsonData.map(video => (
                    <div key={video.highlight_id} className="content">
                        <h4>{video.title}</h4>
                        <p>Date: {video.date}</p>
                        <video controls className='video'>
                            <source src={"http://localhost:5000/" + video.video} type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                    </div>
                ))}
            </div>
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
            </div>
            ) : (
                <p>Loading...</p>
            )};
        </main>
    );
};

export default Main;
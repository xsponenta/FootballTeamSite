import '../static/styles.css';
import background from '../icons/with_fans.jpg'
import logo from '../icons/logo.png'
import enemy from '../icons/enemy.png'
import React, { useState, useEffect } from 'react';

const Main = () => {
    const [jsonData, setData] = useState(null);
    const [lastData, setLastData] = useState(null);
    const [playingVideoId, setPlayingVideoId] = useState(null);
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
        setData(jsonData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
      try {
        const response = await fetch('http://127.0.0.1:5000/api/get_closest_ongoing_match');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const lastData = await response.json();
        setLastData(lastData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    const togglePlay = (id) => {
        const video = document.getElementById(`video-${id}`);
        if (playingVideoId === id) {
            video.pause();
            setPlayingVideoId(null);
        } else {
            if (playingVideoId !== null) {
                document.getElementById(`video-${playingVideoId}`).pause();
            }
            video.play();
            setPlayingVideoId(id);
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

                    <div>
                        {/* Individual video components */}
                        <div class="videos">
                        {jsonData.map(video => (
                                <div class="content">
                                        <video id={`video-${video.highlight_id}`} className='video' onClick={() => togglePlay(video.highlight_id)}>
                                        <source src={"http://localhost:5000/" + video.video} type="video/mp4"/>
                                        Your browser does not support the video tag.
                                    </video>
                                    <h4 className='title'>{video.title}</h4>
                                </div>
                        ))}
                        </div>
                    </div>
                </div>
            ) : (
                <p>Loading...</p>
            )}
            { lastData ? (
            <div className="last-match">
                <div className="controls">
                    <h3>Last match review</h3>
                </div>
                <div className="scoreboard">
                    <div className="score">
                        <img className="our" width="5%" src={logo}></img>
                        <h2 className='command-main'>Petro United</h2>
                        <h2 className='score-only'>{lastData.team_score} : {lastData.rival_score}</h2>
                        <h2 className='command-main'>{lastData.rival_team}</h2>
                        <img className="enemy" width="11%" src={enemy}></img>
                    </div>
                    <div className="preview-button">
                        <a href = {"/match/" + lastData.match_id} ><button className="btn">Watch Review</button></a>
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
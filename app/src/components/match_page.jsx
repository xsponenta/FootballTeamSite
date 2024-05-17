import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import logo from "../icons/logo.png"
import enemy from "../icons/enemy.png"

const MatchPage = () => {
    const [matchData, setMatchesData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const { id } = useParams(); // Get the match ID from the URL
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const [view, setView] = useState('statistics');
    const [playingVideoId, setPlayingVideoId] = useState(null);
    useEffect(() => {
        fetchData();
    }, [id]);
    const fetchData = async () => {
        try {
            const dataToSend = {
                "match_id": id
            };
            const response = await fetch('http://16.171.27.41:5000/api/get_match_info_by_id', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify(dataToSend),
              });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const jsonData = await response.json();
            setMatchesData(jsonData);
            setLoading(false);
        } catch (error) {
            setError(error.message);
            setLoading(false);
        }
    };

    const capitalizeFirstLetter = (str) => {
        return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    };
    const renderMatchInfo = () => (
        <div>
            <ul className = "matches-container">
                <li key={matchData.Match.match_id} className="lst-container">
                    <div className='inner-div'>
                        <p className='date'>{capitalizeFirstLetter(new Date(matchData.Match.start_time).toLocaleDateString(undefined, options))}</p>
                        <div className='score-sect'>
                            <p className='command'>Petro United</p>
                            <div className='score-cont'>
                            <p className='score-label'>Score</p>
                            <p className='score'>{matchData.Match.team_score} : {matchData.Match.rival_score}</p>
                            </div>
                            <p className='command'>{matchData.Match.rival_team}</p>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
      );
    
      const renderStatistics = () => (
        <div class="statistics">
          <h2>СТАТИСТИКА КОМАНДИ</h2>
          <div class="teams">
            <div class="team">
              <div class="team-emblem">
                <img src={logo} alt="Ukraine Team Emblem" />
              </div>
              <div class="team-stats">
                <div class="stat">
                  <span class="label">Удари</span>
                  <span class="value">{matchData.Statistic.hits_team}</span>
                </div>
                <div class="stat">
                  <span class="label">Удари у ворота</span>
                  <span class="value">{matchData.Statistic.hits_gate_team}</span>
                </div>
                <div class="stat">
                  <span class="label">Фоли</span>
                  <span class="value">{matchData.Statistic.falls_team}</span>
                </div>
                <div class="stat">
                  <span class="label">Жовті картки</span>
                  <span class="value">{matchData.Statistic.yellow_cards_team}</span>
                </div>
                <div class="stat">
                  <span class="label">Червоні картки</span>
                  <span class="value">{matchData.Statistic.red_cards_team}</span>
                </div>
                <div class="stat">
                  <span class="label">Кутові</span>
                  <span class="value">{matchData.Statistic.corners_team}</span>
                </div>
              </div>
            </div>
            <div class="team">
              <div class="team-emblem-enemy">
                <img src={enemy} alt="France Team Emblem" />
              </div>
              <div class="team-stats">
                <div class="stat">
                  <span class="label">Удари</span>
                  <span class="value">{matchData.Statistic.hits_rival}</span>
                </div>
                <div class="stat">
                  <span class="label">Удари у ворота</span>
                  <span class="value">{matchData.Statistic.hits_gate_rival}</span>
                </div>
                <div class="stat">
                  <span class="label">Фоли</span>
                  <span class="value">{matchData.Statistic.falls_rivals}</span>
                </div>
                <div class="stat">
                  <span class="label">Жовті картки</span>
                  <span class="value">{matchData.Statistic.yellow_cards_rival}</span>
                </div>
                <div class="stat">
                  <span class="label">Червоні картки</span>
                  <span class="value">{matchData.Statistic.red_cards_rival}</span>
                </div>
                <div class="stat">
                  <span class="label">Кутові</span>
                  <span class="value">{matchData.Statistic.corners_rivals}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      );
    
      const renderPlayers = () => (
        <div className="team-page">
            <div>
                {matchData.Players && Object.entries(matchData.Players).map(([category, players], index) => (
                    <PlayerList key={index} category={category} players={players} />
                ))}
            </div>
        </div>
      );
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
      const renderHighlights = () => (
        <div>
        <div>
            {/* Individual video components */}
            <div class="videos">
            {matchData.Highlights.map((video, index) => (
                <div class="content">
                        <video id={`video-${video.highlight_id}`} className='video' onClick={() => togglePlay(video.highlight_id)}>
                        <source src={"http://16.171.27.41:5000/" + video.video} type="video/mp4"/>
                        Your browser does not support the video tag.
                    </video>
                    <h4 className='title'>{video.title}</h4>
                </div>
            ))}
            </div>
        </div>
    </div>
      );
    return (
        <div>
            {loading ? (
                <p>Loading...</p>
            ) : error ? (
                <p>Error: {error}</p>
            ) : (
                <div className='btns-cont'>
                    <h1 className='match-info'>Match Info</h1>
                    <div >
                        {renderMatchInfo()}
                    <div className='btns'>
                        <button onClick={() => setView('statistics')} className='btn'>Statistics</button>
                        <button onClick={() => setView('players')} className='btn'>Players</button>
                        <button onClick={() => setView('highlights')} className='btn'>Highlights</button>
                    </div >
                        {view === 'statistics' && renderStatistics()}
                        {view === 'players' && renderPlayers()}
                        {view === 'highlights' && renderHighlights()}
                    </div>
                </div>
            )}
        </div>
    );
};
const PlayerList = ({ category, players }) => (
    <div className="player-list">
        <h3>{category}</h3>
        <div className="player-grid">
            {players.map((player, playerIndex) => (
                <div key={playerIndex} className="player-card">
                    <img src={`data:image/jpeg;base64,${player.picture}`} alt="Player"/>
                    <p>{player.first_name} {player.last_name}</p>
                </div>
            ))}
        </div>
    </div>
);
export default MatchPage;

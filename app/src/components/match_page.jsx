import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "../match.css";

const MatchPage = () => {
    const [matchData, setMatchesData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [showOngoingMatches, setShowOngoingMatches] = useState(true);
    const { id } = useParams(); // Get the match ID from the URL
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const [view, setView] = useState('match');
    useEffect(() => {
        fetchData();
    }, [id]);
    const fetchData = async () => {
        try {
            const dataToSend = {
                "match_id": id
            };
            const response = await fetch('http://127.0.0.1:5000/api/get_match_info_by_id', {
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
        <div>
          <h2>Statistics</h2>
          <p>Hits Team: {matchData.Statistic.hits_team}</p>
        </div>
      );
    
      const renderPlayers = () => (
        <div>
          <h2>Players</h2>
          {matchData.Players.map(player => (
            <div key={player.player_id}>
              <p>Player Name: {player.first_name} {player.last_name}</p>
            </div>
          ))}
        </div>
      );
    
      const renderHighlights = () => (
        <div>
          <h2>Highlights</h2>
          {matchData.Highlights.map(highlight => (
            <div key={highlight.highlight_id}>
              <p>Title: {highlight.title}</p>
              <video controls>
                <source src={"http://127.0.0.1:5000/" + highlight.video} type="video/mp4" />
                Your browser does not support the video tag.
              </video>
            </div>
          ))}
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
                    <h1>Match Info</h1>
                    <div>
                        {renderMatchInfo()}
                    <div className='btns'>
                        <button onClick={() => setView('statistics')} className='btn'>Statistics</button>
                        <button onClick={() => setView('players')} className='btn'>Players</button>
                        <button onClick={() => setView('highlights')} className='btn'>Highlights</button>
                    </div>
                        {view === 'statistics' && renderStatistics()}
                        {view === 'players' && renderPlayers()}
                        {view === 'highlights' && renderHighlights()}
                    </div>
                </div>
            )}
        </div>
    );
};

export default MatchPage;

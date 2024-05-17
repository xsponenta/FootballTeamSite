import React, { useState, useEffect } from 'react';
import "../static/matches.css"

const MatchesPage = () => {
    const [matchesData, setMatchesData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [showOngoingMatches, setShowOngoingMatches] = useState(true);
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await fetch('http://16.171.27.41:5000/api/get_all_matches');
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

    const showOngoing = () => {
        setShowOngoingMatches(true);
    };

    const showFinished = () => {
        setShowOngoingMatches(false);
    };
    const capitalizeFirstLetter = (str) => {
        return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    };
    const filteredMatches = matchesData
        ? (showOngoingMatches ? matchesData.filter(match => match.ongoing) : matchesData.filter(match => !match.ongoing))
        : [];

    return (
        <div>
            {loading ? (
                <p>Loading...</p>
            ) : error ? (
                <p>Error: {error}</p>
            ) : (
                <div>
                    <h1>All Matches</h1>
                    <div className='btns-cont'>
                        <div className='btns'>
                            <button onClick={showOngoing} className='btn'>Upcoming</button>
                            <button onClick={showFinished} className='btn'>Past</button>
                        </div>
                        <ul className="matches-container">
                            {filteredMatches.map(match => (
                                <a href={"/match/" + match.match_id} className='link-btn'>
                                    <li key={match.match_id} className="lst-container">
                                        <div className='inner-div'>
                                            <p className='date'>{capitalizeFirstLetter(new Date(match.start_time).toLocaleDateString(undefined, options))}</p>
                                            <div className='score-sect'>
                                                <p className='command'>Petro United</p>
                                                {match.ongoing ? (
                                                    <p className='time'>{new Date(match.start_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</p>
                                                ) : (
                                                    <div className='score-cont'>
                                                        <p className='score-label'>Score</p>
                                                        <p className='score'>{match.team_score} : {match.rival_score}</p>
                                                    </div>
                                                )}
                                                <p className='command'>{match.rival_team}</p>
                                            </div>
                                        </div>
                                    </li>
                                </a>
                            ))}
                        </ul>
                    </div>
                </div>
            )}
        </div>
    );
};

export default MatchesPage;

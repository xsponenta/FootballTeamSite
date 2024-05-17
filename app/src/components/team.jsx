import React, { useState, useEffect } from 'react';
import '../static/team.css';

const PlayerList = ({ category, players }) => (
    <div className="player-list">
        <h3>{category}</h3>
        <div className="player-grid">
            {players.map((player, playerIndex) => (
                <div key={playerIndex} className="player-card">
                    <img src={`data:image/jpeg;base64,${player.picture}`} alt="Player" />
                    <p className='football-title'>{player.first_name} {player.last_name}</p>
                </div>
            ))}
        </div>
    </div>
);

const TeamPage = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await fetch('http://16.171.27.41:5000/api/get_all_player');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const playersData = await response.json();
            const orderedKeys = ["Goalkeeper", "Defender", "Midfielder", "Attacker"];
            const sortedPlayersData = {};
            orderedKeys.forEach(key => {
                sortedPlayersData[key] = playersData[0][key];
            });
            setData([sortedPlayersData]);
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="team-page">
            {loading ? (
                <p>Loading...</p>
            ) : (
                <div>
                    {data && Object.entries(data[0]).map(([category, players], index) => (
                        <PlayerList key={index} category={category} players={players} />
                    ))}
                </div>
            )}
        </div>
    );
};

export default TeamPage;
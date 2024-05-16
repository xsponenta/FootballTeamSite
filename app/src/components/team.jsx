import React, { useState, useEffect } from 'react';
//import TeamCategory from '../components/team.jsx'; // Припускаючи, що у вас є окремий файл для TeamCategory

const TeamPage = () => {
    const [data, setData] = useState(null);
    useEffect(() => {
      fetchData();
    }, []);
  
    const fetchData = async () => {
        try {
          const response = await fetch('http://10.10.243.126:5000/api/get_all_player');
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          const jsonData = await response.json();
          setData(jsonData);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
    return (
        <div>
            {data ? (
                <div>
                    <h2>Data fetched successfully:</h2>
                    {Object.keys(data[0]).map((category, index) => (
                        <div key={index}>
                            <h3>{category}</h3>
                            {data[0][category].map((player, playerIndex) => (
                                <div key={playerIndex}>
                                    <p>{player.first_name}</p>
                                    <img src={'data:image/jpeg;base64,' + player.picture} alt="Player Image"></img>
                                </div>
                            ))}
                        </div>
                    ))}
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default TeamPage;

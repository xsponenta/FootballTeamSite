import React, { useState, useEffect } from 'react';

function Test() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://10.10.240.163:5000/api/get_all_player');
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
          <p>{data[0]["picture"]}</p>
          <img id="player-image" src={'data:image/jpeg;base64,' + data[2]["picture"]} alt="Player Image"></img>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Test;

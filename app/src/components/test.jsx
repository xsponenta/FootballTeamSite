import React, { useState, useEffect } from 'react';

function Test() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://10.10.243.126:5000/api/get_recent_highlights');
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
          <p>{data[0]["date"]}</p>
          <video width="600" controls>
            <source src={"http://10.10.243.126:5000/" + data[0]["video"]} type="video/mp4"/>
          </video>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Test;

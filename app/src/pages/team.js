import React from 'react';
import TeamCategory from '../components/team.jsx'; // Припускаючи, що у вас є окремий файл для TeamCategory

const TeamSection = () => (
    <div className="team-section">
        <h2>Our Team</h2>
            <TeamCategory title="Goalkeepers" members={[{name: 'Player 1', photo: '../Ivanyshyn.jpg'}, {name: 'Player 2', photo: '../Ivanyshyn.jpg'}]} />
            <TeamCategory title="Defenders" members={[{name: 'Player 1', photo: '../Ivanyshyn.jpg'}, {name: 'Player 2', photo: '../Ivanyshyn.jpg'}]} />
            <TeamCategory title="Midfielders" members={[{name: 'Player 1', photo: '../Ivanyshyn.jpg'}, {name: 'Player 2', photo: '../Ivanyshyn.jpg'}]} />
            <TeamCategory title="Attackers" members={[{name: 'Player 1', photo: '../Ivanyshyn.jpg'}, {name: 'Player 2', photo: '../Ivanyshyn.jpg'}]} />
    </div>
);
export default TeamSection;

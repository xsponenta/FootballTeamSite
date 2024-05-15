import React from 'react';
import TeamCategory from './components/team.jsx'; // Припускаючи, що у вас є окремий файл для TeamCategory
import teamData from './components/teamData.jsx'; // Шлях до вашого файлу з даними команди

const TeamSection = () => (
    <div className="team-section">
        <h2>Our Team</h2>
        <TeamCategory title="Goalkeepers" members={teamData.goalkeepers} />
        <TeamCategory title="Defenders" members={teamData.defenders} />
        <TeamCategory title="Midfielders" members={teamData.midfielders} />
        <TeamCategory title="Attackers" members={teamData.attackers} />
    </div>
);

export default TeamSection;

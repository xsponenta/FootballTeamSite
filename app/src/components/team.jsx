import React from 'react';

const TeamMember = (name, photo) => (
    <div className="team-member">
        <div className="member-photo">
            {<img src={photo} alt={name} />}
        </div>
        <div className="member-name">{name}</div>
    </div>
);

const TeamCategory = ({ title, members }) => (
    <div className="team-category">
        <h3>{title}</h3>
        {members.map((member, index) => (
            <TeamMember key={index} name={member.name} photo={member.photo}/>
        ))}
    </div>
);

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
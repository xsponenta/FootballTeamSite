from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Player(Base):
    "Trail model"

    __tablename__ = 'player'

    player_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    position = Column(String, nullable=False)
    picture = Column(String, nullable=False)

    def __repr__(self):
        return f"<Player(first_name = {self.first_name}, last_name = {self.last_name})>"

    def __str__(self):
        return f"<Player(first_name = {self.first_name}, last_name = {self.last_name})>"

class Match(Base):
    "Hike"

    __tablename__ = "match"

    match_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    rival_team = Column(String, nullable=False)
    team_score = Column(Integer, nullable=False, default=0)
    rival_score = Column(Integer, nullable=False, default=0)
    statistics = relationship("Statistic", back_populates="match")
    highlights = relationship("Highlight", back_populates="match")

    def __repr__(self):
        return f'<Match(rival_team = {self.rival_team}, start_time = {self.start_time.strftime("%Y-%m-%d %H:%M:%S")})>'

    def __str__(self):
        return f'<Match(rival_team = {self.rival_team}, start_time = {self.start_time.strftime("%Y-%m-%d %H:%M:%S")})>'

class Relation(Base):
    "Relations"
    
    __tablename__ = "relation"

    relation_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.player_id'), nullable=False)
    match_id = Column(Integer, ForeignKey('match.match_id'), nullable=False)
    player = relationship("Player", backref="relations")
    match = relationship("Match", backref="relations")

    def __repr__(self):
        return f"<Relation(player_id = {self.player_id}, match_id = {self.match_id})>"

    def __str__(self):
        return f"<Relation(player_id = {self.player_id}, match_id = {self.match_id})>"

class Statistic(Base):
    "Statistic"
  
    __tablename__ = "statistic"
    
    statistic_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    hits_team = Column(Integer, nullable=False, default=0)
    hits_rival = Column(Integer, nullable=False, default=0)
    hits_gate_team = Column(Integer, nullable=False, default=0)
    hits_gate_rival = Column(Integer, nullable=False, default=0)
    falls_team = Column(Integer, nullable=False, default=0)
    falls_rivals = Column(Integer, nullable=False, default=0)
    yellow_cards_team = Column(Integer, nullable=False, default=0)
    yellow_cards_rival = Column(Integer, nullable=False, default=0)
    red_cards_team = Column(Integer, nullable=False, default=0)
    red_cards_rival = Column(Integer, nullable=False, default=0)
    offsides_team = Column(Integer, nullable=False, default=0)
    offsides_rivals = Column(Integer, nullable=False, default=0)
    corners_team = Column(Integer, nullable=False, default=0)    
    corners_rivals = Column(Integer, nullable=False, default=0)
    match_id = Column(Integer, ForeignKey('match.match_id'), nullable=False)
    match = relationship("Match", back_populates="statistics")

class Highlight(Base):
    "Highlight"
    
    __tablename__ = "highlight"

    highlight_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    video = Column(String, nullable=False)
    title = Column(String, nullable=False)
    match_id = Column(Integer, ForeignKey('match.match_id'), nullable=False)
    match = relationship("Match", back_populates="highlights")

class Email(Base):
    "Email"
    
    __tablename__ = "email"
    
    email_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    email = Column(String, nullable=False)

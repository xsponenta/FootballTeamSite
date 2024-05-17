import React from 'react';
import Header from '../components/header';
import MatchPage from '../components/match_page';
import Subscribe from '../components/subscribe';
import Footer from '../components/footer';
import { useParams } from 'react-router-dom';

const Match = () => {
  const { id } = useParams();
  return (
    <div>
      <Header />
      <MatchPage />
      <Subscribe />
      <Footer />
    </div>
  );
};

export default Match;
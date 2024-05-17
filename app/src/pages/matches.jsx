import React from 'react';
import Header from '../components/header';
import MatchesPage from '../components/matches_page';
import Subscribe from '../components/subscribe';
import Footer from '../components/footer';

const Matches = () => {
  return (
    <div>
      <Header />
      <MatchesPage />
      <Subscribe />
      <Footer />
    </div>
  );
};

export default Matches;
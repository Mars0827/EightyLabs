import { useState } from 'react';
import Header from './components/Header.jsx';
import HeroSection from './components/HeroSection.jsx';
import BenefitsSection from './components/BenefitsSection.jsx';
import ScanPage from './components/ScanPage.jsx';

const App = () => {
  const [currentPage, setCurrentPage] = useState('home');

  return (
    <div className="min-h-screen flex flex-col">
      <Header currentPage={currentPage} setCurrentPage={setCurrentPage} />
      {currentPage === 'home' && (
        <>
          <HeroSection setCurrentPage={setCurrentPage} />
          <BenefitsSection setCurrentPage={setCurrentPage} />
        </>
      )}
      {currentPage === 'scan' && <ScanPage setCurrentPage={setCurrentPage} />}
    </div>
  );
};

export default App;

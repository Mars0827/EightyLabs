const HeroSection = ({ setCurrentPage }) => {
    return (
      <section className="bg-blue-900 text-white pt-8 pb-16 px-8 relative overflow-hidden flex-grow">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row">
          <div className="md:w-1/2 z-10">
            <h2 className="text-5xl font-bold mb-8">Say No To Poultry Diseases!</h2>
            <div className="mb-8">
              <h3 className="text-2xl mb-4">Say No To Poultry Diseases!</h3>
              <p className="text-xl mb-2">
                Check your chicken's health on the smartphone and get instant results within <span className="font-bold">1 minute</span>.
              </p>
            </div>
            <button 
              onClick={() => setCurrentPage('scan')} 
              className="bg-red-500 hover:bg-red-600 text-white font-bold py-4 px-12 rounded-full text-xl uppercase transition-colors duration-300"
            >
              CHECK NOW
            </button>
            <p className="mt-12 text-sm opacity-80">
              * The scan result is not a diagnosis. To obtain an accurate diagnosis and a recommendation for treatment - consult your veterinarian.
            </p>
          </div>
  
          <div className="md:w-1/2 relative">
            <div className="absolute right-0 top-0 w-full h-full flex items-center">
              <div className="relative">
                <div className="border-2 border-white rounded-lg w-48 h-48 absolute -top-24 right-24">
                  <div className="bg-white/10 w-full h-full rounded-lg"></div>
                </div>
                <div className="mt-12 ml-12">
                  <p className="text-sm mb-2">
                    Take a photo of chicken feces<br />
                    and receive your risk<br />
                    assessment *
                  </p>
                </div>
              </div>
              <img 
                src="/api/placeholder/500/700" 
                alt="Chicken health examination" 
                className="object-cover h-full ml-auto"
              />
            </div>
  
            <div className="absolute bottom-4 right-4">
              <div className="bg-white p-1 rounded-md">
                <img src="/api/placeholder/100/40" alt="Certification" className="h-8" />
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  };
  
  export default HeroSection;
  
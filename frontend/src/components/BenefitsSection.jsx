const BenefitsSection = ({ setCurrentPage }) => {
    return (
      <section className="py-12 px-8 bg-gray-50">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row gap-6">
          <div className="md:w-1/3 p-6 bg-indigo-500 rounded-xl text-white">
            <div className="flex justify-center items-center h-48">
              <span className="text-9xl">?</span>
            </div>
          </div>
          
          <div className="md:w-2/3 bg-cyan-400 rounded-xl p-8 text-white">
            <div className="flex items-center mb-6">
              <div className="mr-4">
                <div className="w-16 h-16 bg-yellow-300 rounded-full flex items-center justify-center text-3xl">
                  ⭐
                </div>
              </div>
              <h3 className="text-4xl font-bold">Get your personal benefits!</h3>
            </div>
  
            <div className="flex space-x-8 mb-8">
              {[
                { icon: '⏱️', label: 'Fast Results' },
                { icon: '🖼️', label: 'Simple Upload' },
                { icon: '📝', label: 'Track Health Records' },
              ].map(({ icon, label }) => (
                <div key={label} className="flex items-center">
                  <div className="w-10 h-10 bg-white rounded-full flex items-center justify-center mr-2">
                    {icon}
                  </div>
                  <span>{label}</span>
                </div>
              ))}
            </div>
  
            <div className="flex justify-center">
              <button 
                onClick={() => setCurrentPage('register')} 
                className="bg-red-500 hover:bg-red-600 text-white font-bold py-3 px-12 rounded-full text-xl uppercase transition-colors duration-300"
              >
                REGISTER
              </button>
            </div>
          </div>
        </div>
      </section>
    );
  };
  
  export default BenefitsSection;
  
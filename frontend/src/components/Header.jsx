const Header = ({ currentPage, setCurrentPage }) => {
    return (
      <header className="bg-blue-900 text-white py-4 px-8">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div 
            className="flex items-center space-x-3 cursor-pointer" 
            onClick={() => setCurrentPage('home')}
          >
            <div className="w-12 h-12 bg-white rounded-lg flex items-center justify-center">
              <div className="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
                <div className="w-4 h-4 bg-white rounded-full"></div>
              </div>
            </div>
            <div>
              <h1 className="text-2xl font-bold">Eightylabs</h1>
              <span className="text-sm">Poultry Health Scanner</span>
            </div>
          </div>
          
          <nav className="hidden md:flex space-x-6">
            {[
              { label: "Main", page: "home" },
              { label: "Risks Detection", page: "risks" },
              { label: "Features", page: "features" },
              { label: "How it works", page: "how-it-works" },
              { label: "Artificial Intelligence", page: "ai" },
              { label: "FAQ", page: "faq" },
              { label: "Register", page: "register" },
              { label: "Log In", page: "login" },
            ].map(({ label, page }) => (
              <a
                key={page}
                href="#"
                onClick={(e) => {
                  e.preventDefault();
                  setCurrentPage(page);
                }}
                className={`hover:text-blue-200 ${currentPage === page ? 'text-blue-200' : ''}`}
              >
                {label}
              </a>
            ))}
          </nav>
        </div>
      </header>
    );
  };
  
  export default Header;
  
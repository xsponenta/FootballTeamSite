import '../styles.css';

const Header = () => {
    return (
        <header className="header">
            <div className="logo"></div>
            <nav>
                <a href="#">Our Team</a>
                <a href="#">Matches</a>
                <a href="#">Shop</a>
                <a href="#">Highlights</a>
                <a href="#">About Us</a>
                <a href="#">Contacts</a>
            </nav>
            <div className="lang">
                <label htmlFor="lang-select">Language:</label>
                <select id="lang-select">
                    <option value="en">EN</option>
                    <option value="es">ES</option>
                </select>
            </div>
        </header>
    );
};

export default Header;
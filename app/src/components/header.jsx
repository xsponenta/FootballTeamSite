import '../styles.css';
import logo from '../logo.png'

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <img src={logo}></img>
            </div>
            <nav>
                <a href="#">Our Team</a>
                <a href="#">Matches</a>
                <a href="#">Shop</a>
                <a href="#">Highlights</a>
                <a href="#">About Us</a>
                <a href="#">Contacts</a>
            </nav>
        </header>
    );
};

export default Header;
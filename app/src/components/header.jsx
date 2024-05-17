import '../styles.css';
import logo from '../logo.png'

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <a href = "/"><img src={logo}></img></a>
            </div>
            <nav>
                <a href="/players">Our Team</a>
                <a href="/matches">Matches</a>
                <a href="#">Highlights</a>
                <a href="#">About Us</a>
                <a href="#">Contacts</a>
            </nav>
        </header>
    );
};

export default Header;
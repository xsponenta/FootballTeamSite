import '../static/styles.css';
import logo from '../icons/logo.png'

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <a href="/"><img src={logo}></img></a>
            </div>
            <nav>
                <a href="/players">Our Team</a>
                <a href="/matches">Matches</a>
                <a href="#AboutUs">About Us</a>
                <a href="#AboutUs">Contacts</a>
            </nav>
        </header>
    );
};

export default Header;
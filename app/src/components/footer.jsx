import '../styles.css';
import tiktok from '../tiktok.png'
import facebook from '../facebook.png'
import insta from '../insta.png'

const Footer = () => {
    return (
        <footer className="footer">
            <div className='links'>
                <div>
                    <p>Links</p>
                </div>
                <div className='services'>
                    <a href="#"><img src={tiktok}></img></a>
                    <a href="#"><img src={facebook}></img></a>
                    <a href="#"><img src={insta}></img></a>
                </div>
            </div>
            <div className='sponsors'>
                <div>
                    <p>Sponsors</p>
                </div>
                <div className='sponsors-list'>
                    <p>Sponsor 1</p>
                    <p>Sponsor 2</p>
                    <p>Sponsor 3</p>
                </div>
            </div>
            <div className='contacts'>
                <div>
                    <p>Contact Us</p>
                </div>
                <div className='fields'>
                    <a href="#">About Us</a>
                    <a href="#">Work with Us</a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
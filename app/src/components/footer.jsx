import '../static/styles.css';
import tiktok from '../icons/tiktok.png'
import kfc from "../icons/kfc.jpg"
import revo from "../icons/revo.jpeg"
import phillip from "../icons/phillip.png"

const Footer = () => {
    return (
        <footer className="footer" id="AboutUs">
            <div className='links'>
                <a href="https://www.tiktok.com/@petro_united?_t=8mPynBO1Wbu&_r=1" className='icon'><img src={tiktok} className='icon'></img></a>
            </div>
            <div className='sponsors'>
                <div className='sponsors-list'>
                    <img src={kfc} className="sponsor-img-kfc"></img>
                    <img src={revo} className="sponsor-img-revo"></img>
                    <img src={phillip} className="sponsor-img-phillip"></img>
                </div>
            </div>
            <div className='contacts'>
                <div>
                    <p>Contact Us</p>
                </div>
                <div className='fields'>
                    <a href="#" className='links'>About Us</a>
                    <a href="#" className='links'>Work with Us</a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
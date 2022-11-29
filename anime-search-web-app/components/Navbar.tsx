import Link from 'next/link'
import Searchbar from './Searchbar'
import styles from '../styles/Navbar.module.css'


const Navbar = () => {
    return (
        <nav id={styles.topNav}>
            <div id={styles.navContent} className='container px-0'>
                {/* drop down icon */}
                <div className={styles.navItem}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" id={styles.sideExpand} className="bi bi-list" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
                    </svg>
                </div>
                <div className={styles.navItem}>
                    <Searchbar />
                </div>
            </div>
        </nav>
    )
}

export default Navbar;
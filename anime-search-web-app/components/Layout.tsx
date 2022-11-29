import Footer from './Footer';
import Navbar from './Navbar'

const Layout = ({ children }: {children: any}) => {
    return (
        <>
            <Navbar /> 
            <main>{children}</main>
            <Footer />
        </>
    );
};

export default Layout;
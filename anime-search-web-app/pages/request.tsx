import Axios from 'axios'

const Request = ({ animeData }: {animeData: any}) => {
    console.log(animeData)
    return(
        <div>hello</div>
    )
};

export const getStaticProps = async () => {
    let api_endpoint: string = 'https://api.jikan.moe/v4/anime/1/full'
    const data = await Axios.get(api_endpoint);

    return {
        props: {
            animeData: data.data
        }
    }
}

export default Request;
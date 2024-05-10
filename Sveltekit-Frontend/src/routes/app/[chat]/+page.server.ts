import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from '$env/static/public';

export const load = async ({ params, cookies }: { params: any, cookies: any }) => {
    const credentials = JSON.parse(cookies.get("credentials"));
    const username = credentials.username;
    // console.log(username);
    const { chat: receiver } = params;
    return {
        props: {
            receiver: receiver,
            username: username,
        }
    };
};

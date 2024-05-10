import { redirect } from '@sveltejs/kit';
import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from '$env/static/public';

export const actions = {
    login: async ({ request, cookies }: { request: any, cookies: any}) => {
        const body = Object.fromEntries(await request.formData());
        try{
            const isloggedin = dblogin(body.username, body.password);
            if(!isloggedin){
                throw Error("Could not log in");
            }
            cookies.set('credentials', JSON.stringify({
                username: body.username,
                password: body.password
            }), {
                path: '/',
                httpOnly: true,
                sameSite: 'strict',
                maxAge: 60 * 60 * 24 * 7
            });
        } catch(err){
            console.error("Error: ", err);
            return {
                notVerified: true
            };
        }
        
        throw redirect(303, "/app/");
    },
    gotoRegister: () => {
        throw redirect(303, "/auth/register");
    }
}

const dblogin = async (username: string, password: string) => {
    try{
        const response = await fetch(`http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/log-in`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password
            })
        });
        if(!response.ok){
            throw Error("Could not log in");
        }
        return true;
    } catch(err){
        console.error("Could not log in: ", err);
        return false;
    }
}
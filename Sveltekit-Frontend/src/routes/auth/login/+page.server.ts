import { redirect } from '@sveltejs/kit';
import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from '$env/static/public';

export const actions = {
    login: async ({ locals, request }: {locals: any, request: any}) => {
        const body = Object.fromEntries(await request.formData());

        try{
            dblogin(body.username, body.password);
            locals.username = body.username;
            locals.password = body.password;
        } catch(err){
            console.error("Error: ", err);
            return {
                notVerified: true
            };
        }
        
        throw redirect(303, "/app/");
    }
}

const dblogin = async (username: string, password: string) => {
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
}
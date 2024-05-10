import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from '$env/static/public';
import { redirect } from '@sveltejs/kit';

export const actions = {
    register: async ({ request }: { locals: any, request: any }) => {
        const body = Object.fromEntries(await request.formData());
        try {
            const flag = dbregister(body.username, body.name, body.password);
            if(!flag) throw Error("Registration unsuccessful");
        } catch (err) {
            console.error("Error: ", err);
            throw Error("Could not Register the New ID");
        }

        throw redirect(303, "/auth/login");
    },
    gotoLogin: () => {
        throw redirect(303, "/auth/login");
    },
};

const dbregister = async (username: string, name: string, password: string) => {
    try {
        const response = await fetch(`http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/sign-up`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                name,
                password
            })
        })
        if (!response.ok) {
            throw Error("Could not register")
        }
        return true;
    } catch(err){
        return false;
    }
}
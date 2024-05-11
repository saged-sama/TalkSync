import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from '$env/static/public';
import { redirect } from '@sveltejs/kit';

export const actions = {
    register: async ({ request }: { locals: any, request: any }) => {
        // console.log(await request.formData());
        const body = Object.fromEntries(await request.formData());
        // console.log(typeof body.image);
        try {
            const flag = dbregister(body.username, body.name, body.password, body.image);
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

const dbregister = async (username: string, name: string, password: string, image: File) => {
    try {
        const img = new Uint8Array(await image.arrayBuffer())
        const type = image.type;
        const siz = image.size;
        if(siz > 25000000){
            throw Error("Image file should not exceed 25MB limit");
        }
        const res = await fetch(`http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/set-profile-picture`, {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                image: img.toString(),
                type: type
            })
        });
        if(!res.ok){
            throw Error("Could not register");
        }
        const resp = await res.json();
        const imgpath = resp.image;

        const response = await fetch(`http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/sign-up`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                name: name,
                password: password,
                image: imgpath
            })
        })
        if (!response.ok) {
            throw Error("Could not register");
        }
        return true;
    } catch(err){
        return false;
    }
}
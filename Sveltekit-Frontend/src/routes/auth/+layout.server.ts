import { redirect } from "@sveltejs/kit";

export const load = ({ cookies }: {cookies: any}) => {
    const cred = cookies.get("credentials");
    if(cred){
        throw redirect(303, "/app/");
    }
    return {};
}
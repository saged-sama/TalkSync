import { redirect } from "@sveltejs/kit";

export const load = async ({ params, cookies }: { params: any, cookies: any }) => {
    const cred = cookies.get("credentials");
    if (!cred) {
        throw redirect(303, "/auth/login");
    }
    const credentials = JSON.parse(cred);
    const { chat: chatid } = params;
    return {
        username: credentials.username,
        chatid: chatid
    };
};
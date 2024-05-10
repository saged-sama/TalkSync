import { redirect } from "@sveltejs/kit";

export const POST = async ({ cookies }: {cookies: any}) => {
    cookies.set('credentials', '', {
        path: '/',
        httpOnly: true,
        sameSite: 'strict',
        maxAge: 0
    });
    throw redirect(303, "/auth/login");
};
import { redirect } from "@sveltejs/kit";

export const POST = async ({ locals }: {locals: any}) => {
    locals.cookies.username = undefined;
    locals.cookies.password = undefined;
    locals.username = undefined;
    
    throw redirect(303, "/auth/login");
}
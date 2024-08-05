import { Error, Login, Main, Users, Station, Overview } from "@pagesReact";
import { StationMain, StationPeople } from "@componentsReact";

import {
    Route,
    createBrowserRouter,
    RouterProvider,
    createRoutesFromElements,
} from "react-router-dom";

import { ProtectedRoute, UnprotectedRoute } from "@routes/index";
import { AuthProvider } from "@hooks/useAuth";

const router = createBrowserRouter(
    createRoutesFromElements(
        <>
            <Route path="/auth" element={<UnprotectedRoute />}>
                <Route path="login" element={<Login />} />
                <Route path="*" element={<Error />} />
            </Route>
            <Route
                path="/"
                element={<ProtectedRoute />}
                handle={{
                    crumb: () => {
                        return "Home";
                    },
                }}
            >
                <Route index element={<Main />} />
                <Route
                    path="overview"
                    element={<Overview />}
                    handle={{
                        crumb: () => {
                            return "overview";
                        },
                    }}
                />
                <Route
                    path="users"
                    element={<Users />}
                    handle={{
                        crumb: () => {
                            return "Users";
                        },
                    }}
                />
                <Route
                    path=":nc/:sc"
                    element={<Station />}
                    handle={{
                        crumb: () => {
                            return "Station";
                        },
                    }}
                >
                    <Route index element={<StationMain />} />
                    <Route
                        path="people"
                        element={<StationPeople />}
                        handle={{
                            crumb: () => {
                                return "People";
                            },
                        }}
                    />
                </Route>
                <Route path="*" element={<Error />} />
            </Route>
        </>,
    ),
);

function App() {
    return (
        <AuthProvider>
            <RouterProvider router={router} />
        </AuthProvider>
    );
}

export { router };
export default App;

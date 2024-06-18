export const STATION_INFO_STATE = {
    api_id: "",
    network_code: "",
    station_code: "",
    receiver_code: "",
    receiver_serial: "",
    receiver_firmware: "",
    antenna_code: "",
    antenna_serial: "",
    antenna_height: 0,
    antenna_north: 0,
    antenna_east: 0,
    height_code: "",
    radome_code: "",
    date_start: "",
    date_end: "",
    receiver_vers: "",
    comments: null,
};

type UserState = {
    id: null | number;
    username: string;
    password: string;
    role: {
        id: null | number;
        name: string;
    };
    is_active: null | boolean;
    first_name: string;
    last_name: string;
    email: string;
    phone: string;
    address: string;
    photo: string;
    [key: string]: any; // Añade esta línea
};

export const USERS_STATE: UserState = {
    id: null,
    username: "",
    password: "",
    role: {
        id: null,
        name: "",
    },
    is_active: null,
    first_name: "",
    last_name: "",
    email: "",
    phone: "",
    address: "",
    photo: "",
};

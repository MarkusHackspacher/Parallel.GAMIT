import { useEffect, useState } from "react";
import { LatLngExpression } from "leaflet";
import {
    Map,
    SearchInput,
    Sidebar,
    Skeleton,
    Spinner,
    StationsModal,
} from "@componentsReact";

import useApi from "@hooks/useApi";
import { useAuth } from "@hooks/useAuth";

import { getStationsService } from "@services";
import { ChevronLeftIcon } from "@heroicons/react/24/outline";
import { GetParams, StationData, StationServiceData } from "@types";
import { useLocation } from "react-router-dom";

const MainPage = () => {
    const { token, logout } = useAuth();
    const api = useApi(token, logout);

    const location = useLocation();

    const windowState = window.history.state.usr as StationData;

    const locationState =
        location.state && windowState
            ? windowState
            : (location.state as StationData);

    const [station, setStation] = useState<StationData | undefined>(undefined);
    const [stations, setStations] = useState<StationData[] | undefined>(
        undefined,
    );
    const [initialStations, setInitialStations] = useState<
        StationData[] | undefined
    >(undefined);
    const [initialCenter, setInitialCenter] = useState<
        LatLngExpression | undefined
    >(undefined);

    const [list, setList] = useState<boolean>(false);

    const [loading, setLoading] = useState<boolean>(true);
    const [spinner, setSpinner] = useState<boolean>(false);

    const getInitialStations = async () => {
        try {
            setLoading(true);
            const result = await getStationsService<StationServiceData>(
                api,
                params,
            );
            if (result) {
                setInitialStations(result.data);
            }
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const getStations = async () => {
        setSpinner(true);

        try {
            // if (!params.country_code || !params.network_code) return;
            const result = await getStationsService<StationServiceData>(
                api,
                params,
            );
            if (result) {
                setStations(result.data);
                if (result.data?.length > 0) {
                    setInitialCenter([result.data[0].lat, result.data[0].lon]);
                }
            }
        } catch (err) {
            console.error(err);
        } finally {
            setSpinner(false);
        }
    };

    // const [showStations, setShowStations] = useState<boolean>(false);
    const [showSidebar, setShowSidebar] = useState<boolean>(false);

    const [params, setParams] = useState<GetParams>({
        country_code: "",
        network_code: "",
        station_code: "",
        limit: 0,
        offset: 0,
    });

    useEffect(() => {
        if (
            (initialStations &&
                params.station_code === " " && // PARAMS RESETEADOS
                params.country_code === " " &&
                params.network_code === " ") ||
            (params.station_code === "" && // PARAMS RESETEADOS
                params.country_code === "" &&
                params.network_code === "")
        ) {
            setStations(initialStations);
        }

        if (
            initialStations &&
            (params.country_code?.trim() !== "" ||
                params.network_code?.trim() !== "" ||
                params.station_code?.trim() !== "")
        ) {
            getStations();
        }
    }, [params]);

    useEffect(() => {
        if (!initialStations) {
            // FIXME: Corresponder las initialstations al rango de la vista
            //que el usuario tenga determinada ??¿¿, seguro tenga que hacer un nuevo getStations
            getInitialStations();
        }
    }, []);

    useEffect(() => {
        const stateCoordinates =
            locationState !== null && Object.values(locationState).length > 0
                ? ([locationState?.lat, locationState?.lon] as LatLngExpression)
                : undefined;

        if (stateCoordinates) {
            setInitialCenter(stateCoordinates);
        }
    }, [locationState]);

    return (
        <div className={"my-auto flex flex-1 transition-all duration-200"}>
            {loading ? (
                <Skeleton />
            ) : (
                <>
                    <Sidebar
                        show={showSidebar}
                        setShow={setShowSidebar}
                        station={station}
                    />
                    <div
                        className={"self-center w-full flex flex-col flex-wrap"}
                    >
                        <div
                            className={`absolute right-0 z-50 h-4/6 flex items-center`}
                        >
                            {" "}
                            <button
                                className="btn"
                                style={{
                                    writingMode: "vertical-rl",
                                    width: "50px",
                                    height: "200px",
                                    fontSize: "18px",
                                }}
                                onClick={() => {
                                    setList(!list);
                                }}
                            >
                                {" "}
                                Station lists
                                <ChevronLeftIcon className="h-6 w-6" />
                            </button>{" "}
                        </div>
                        <div className="flex justify-center flex-wrap items-center">
                            <SearchInput
                                stations={stations}
                                params={params}
                                setParams={setParams}
                                setStation={setStation}
                            />
                        </div>
                        {spinner && (
                            <div className="absolute mt-28 right-52 z-50">
                                {" "}
                                <Spinner size={"lg"} />
                            </div>
                        )}
                        <Map
                            stations={stations ? stations : initialStations}
                            initialCenter={initialCenter}
                        />
                        {list && (
                            <div
                                className={`fixed right-20   
                                transition-all mt-[88px] h-fit flex z-50 `}
                            >
                                <StationsModal
                                    setState={setList}
                                    stations={stations}
                                />
                            </div>
                        )}
                    </div>
                </>
            )}
        </div>
    );
};

export default MainPage;

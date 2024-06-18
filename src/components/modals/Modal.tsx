import { modalSizes } from "@utils/index";
import { ReactNode } from "react";

interface ModalProps {
    close: boolean;
    modalId: string;
    size?: "sm" | "smPlus" | "md" | "lg" | "xl" | "fit";
    handleCloseModal?: () => void;
    setModalState?: React.Dispatch<
        React.SetStateAction<
            | { show: boolean; title: string; type: "add" | "edit" | "none" }
            | undefined
        >
    >;
    children: ReactNode;
}

const Modal = ({
    close,
    modalId,
    size,
    handleCloseModal,
    setModalState,
    children,
}: ModalProps) => {
    return (
        <dialog id={modalId + "-modal"} className="modal">
            <div
                className="modal-box"
                style={{ maxWidth: "", minWidth: size ? modalSizes[size] : "" }}
            >
                {close && (
                    <form method="dialog">
                        <button
                            className="btn btn-sm btn-circle btn-ghost absolute top-2 right-2"
                            onClick={() => {
                                handleCloseModal ? handleCloseModal() : null;
                                setModalState ? setModalState(undefined) : null;
                            }}
                        >
                            ✕
                        </button>
                    </form>
                )}
                {children}
            </div>
            {!close && (
                <form method="dialog" className="modal-backdrop ">
                    <button
                        onClick={() => {
                            handleCloseModal ? handleCloseModal() : null;
                            setModalState ? setModalState(undefined) : null;
                        }}
                    >
                        close
                    </button>
                </form>
            )}
        </dialog>
    );
};

export default Modal;

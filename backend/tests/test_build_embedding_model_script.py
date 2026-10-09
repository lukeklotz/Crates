import pytest

from crate_backend.scripts.build_embedding_model import parse_args


def test_defaults():
    args = parse_args([])

    assert args.alpha == 0.6
    assert args.device == "cpu"
    assert args.batch_size == 64
    assert args.out is None
    assert not args.no_reception and not args.no_personnel


def test_flags_are_read(tmp_path):
    args = parse_args(
        [
            "--alpha",
            "0.4",
            "--no-reception",
            "--no-personnel",
            "--device",
            "mps",
            "--batch-size",
            "16",
            "--out",
            str(tmp_path / "x.joblib"),
        ]
    )

    assert (args.alpha, args.device, args.batch_size) == (0.4, "mps", 16)
    assert args.no_reception and args.no_personnel
    assert args.out == tmp_path / "x.joblib"


def test_alpha_outside_zero_one_is_rejected():
    with pytest.raises(SystemExit):
        parse_args(["--alpha", "1.5"])

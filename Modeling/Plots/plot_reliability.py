"""
Plot Reliability Transitoria - Progetto Mobius
Design: mu fisso, lambda variabile. Dimostra invarianza rispetto a mu.
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

os.makedirs("plot/ita", exist_ok=True)
os.makedirs("plot/en",  exist_ok=True)

# ── Dati ─────────────────────────────────────────────────────────────────────
time_instants = [24, 360, 1080, 2520, 5400, 11160]

experiments_rel = [
    (1,  0.01,   0.01,   9.416533e-001, 1.458947e-001, 5.606235e-004, 8.585941e-009, 1.513222e-018, 2.629008e-038),
    (2,  0.001,  0.01,   9.940180e-001, 9.132555e-001, 7.251091e-001, 3.200976e-001, 3.566162e-002,  4.242178e-004),
    (3,  1e-4,   0.01,   9.994002e-001, 9.910412e-001, 9.733593e-001, 9.387988e-001, 8.698593e-001,  7.136483e-001),
    (4,  0.01,   0.001,  9.416533e-001, 1.458947e-001, 5.606235e-004, 8.585941e-009, 1.513222e-018, 2.629008e-038),
    (5,  0.001,  0.001,  9.940180e-001, 9.132488e-001, 7.251044e-001, 3.200974e-001, 3.671699e-002,  4.164312e-004),
    (6,  1e-4,   0.001,  9.994002e-001, 9.910407e-001, 9.733589e-001, 9.388013e-001, 8.701656e-001,  7.144800e-001),
    (7,  0.01,   1e-4,   9.416533e-001, 1.458947e-001, 5.606235e-004, 8.585941e-009, 1.513222e-018, 2.629008e-038),
    (8,  0.001,  1e-4,   9.940180e-001, 9.132488e-001, 7.251044e-001, 3.200974e-001, 3.671699e-002,  4.164312e-004),
    (9,  1e-4,   1e-4,   9.994002e-001, 9.910405e-001, 9.733614e-001, 9.388061e-001, 8.701659e-001,  7.144825e-001),
]

lambdas = sorted(set(e[1] for e in experiments_rel))
mus     = sorted(set(e[2] for e in experiments_rel), reverse=True)

# ── Stile dark ────────────────────────────────────────────────────────────────
style = {
    "figure.facecolor": "#0F172A", "axes.facecolor": "#1E293B",
    "axes.edgecolor":   "#475569", "axes.labelcolor": "#E2E8F0",
    "xtick.color":      "#94A3B8", "ytick.color":    "#94A3B8",
    "grid.color":       "#334155", "grid.linestyle": "--", "grid.alpha": 0.5,
    "text.color":       "#E2E8F0",
    "legend.facecolor": "#1E293B", "legend.edgecolor": "#475569",
    "legend.labelcolor":"#E2E8F0",
}
matplotlib.rcParams.update(style)
matplotlib.rcParams["font.family"] = "DejaVu Sans"

# ── Palette ───────────────────────────────────────────────────────────────────
LAM_COLORS   = {0.01: "#DC2626", 0.001: "#D97706", 1e-4: "#16A34A"}
LAM_MARKERS  = {0.01: "v",       0.001: "s",        1e-4: "o"}
MU_LINESTYLE = {0.01: "-",       0.001: "--",        1e-4: ":"}
MU_COLORS_OV = {0.01: "#60A5FA", 0.001: "#A78BFA",  1e-4: "#34D399"}

# ── Helpers ───────────────────────────────────────────────────────────────────
def lam_sym(v):
    m = {0.01: "10\u207b\u00b2", 0.001: "10\u207b\u00b3", 1e-4: "10\u207b\u2074"}
    return m[v]

def mu_sym(v):
    return lam_sym(v)  # same format

def get_exp(lam, mu):
    for e in experiments_rel:
        if e[1] == lam and e[2] == mu:
            return e

TEXTS = {
    "ita": {
        "saved":        "Salvato:",
        "time_xlabel":  "Tempo [h]",
        "rel_ylabel":   "Reliability R(t)",
        "log_ylabel":   "Reliability R(t) [scala log]",
        "linear_title": "Reliability R(t) vs Tempo\n\u03bc fisso = {mu}  |  variazione di \u03bb",
        "log_title":    "Reliability R(t) vs Tempo (scala log)\n\u03bc fisso = {mu}  |  variazione di \u03bb",
        "inv_title":    "Invarianza di R(t) rispetto a \u03bc\n\u03bb fisso = {lam}  \u2014  le curve devono coincidere",
        "inv_lin":      "Scala Lineare",
        "inv_log":      "Scala Logaritmica",
        "heat_title":   "Heatmap Reliability R(t={t}h)\nGriglia \u03bb \u00d7 \u03bc \u2014 Bande Verticali = Invarianza di \u03bc",
        "heat_xlabel":  "Failure Rate  \u03bb  [h\u207b\u00b9]",
        "heat_ylabel":  "Repair Rate  \u03bc  [h\u207b\u00b9]",
        "bar_title":    "Degrado Reliability R(t) \u2014 \u03bc fisso = {mu}",
        "bar_xlabel":   "Istante di tempo [h]",
        "bar_note":     "Barre troncate a 0.01% per valori < 1e-4",
        "lam_legend":   "\u03bb = {lam}  (Exp {exp})",
        "mu_legend":    "\u03bc = {mu}  (Exp {exp})",
    },
    "en": {
        "saved":        "Saved:",
        "time_xlabel":  "Time [h]",
        "rel_ylabel":   "Reliability R(t)",
        "log_ylabel":   "Reliability R(t) [log scale]",
        "linear_title": "Reliability R(t) vs Time\nFixed \u03bc = {mu}  |  varying \u03bb",
        "log_title":    "Reliability R(t) vs Time (log scale)\nFixed \u03bc = {mu}  |  varying \u03bb",
        "inv_title":    "Invariance of R(t) w.r.t. \u03bc\nFixed \u03bb = {lam}  \u2014  curves must coincide",
        "inv_lin":      "Linear Scale",
        "inv_log":      "Log Scale",
        "heat_title":   "Heatmap Reliability R(t={t}h)\nGrid \u03bb \u00d7 \u03bc \u2014 Vertical Bands = Invariance of \u03bc",
        "heat_xlabel":  "Failure Rate  \u03bb  [h\u207b\u00b9]",
        "heat_ylabel":  "Repair Rate  \u03bc  [h\u207b\u00b9]",
        "bar_title":    "Reliability R(t) Degradation \u2014 Fixed \u03bc = {mu}",
        "bar_xlabel":   "Time instant [h]",
        "bar_note":     "Bars clamped to 0.01% for values < 1e-4",
        "lam_legend":   "\u03bb = {lam}  (Exp {exp})",
        "mu_legend":    "\u03bc = {mu}  (Exp {exp})",
    },
}

for lang, T in TEXTS.items():
    D = f"plot/{lang}"

    # ── PLOT 1 & 2: per ogni mu fisso, curva R(t) al variare di lambda ────────
    for mu in mus:
        mu_s = mu_sym(mu)

        for scale in ("linear", "log"):
            fig, ax = plt.subplots(figsize=(10, 6))
            title_key = "linear_title" if scale == "linear" else "log_title"
            fig.suptitle(T[title_key].format(mu=mu_s),
                         fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)

            for lam in sorted(lambdas):
                e = get_exp(lam, mu)
                rv = list(e[3:])
                rv_clip = [max(v, 1e-38) for v in rv]
                label = T["lam_legend"].format(lam=lam_sym(lam), exp=e[0])

                ax.plot(time_instants, rv_clip if scale == "log" else rv,
                        marker=LAM_MARKERS[lam], color=LAM_COLORS[lam],
                        linewidth=2.5, markersize=8, label=label)

                if scale == "linear":
                    # annotazione valore al tempo finale
                    ax.annotate(f"{rv[-1]:.2e}",
                                xy=(time_instants[-1], rv[-1]),
                                xytext=(5, 0), textcoords="offset points",
                                fontsize=8, color=LAM_COLORS[lam], alpha=0.9)

            ax.set_xlabel(T["time_xlabel"], fontsize=12)
            if scale == "linear":
                ax.set_ylabel(T["rel_ylabel"], fontsize=12)
                ax.set_ylim(-0.05, 1.05)
                ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
            else:
                ax.set_yscale("log")
                ax.set_ylabel(T["log_ylabel"], fontsize=12)
                ax.grid(True, which="both", linestyle="--", alpha=0.3)

            ax.grid(True)
            ax.legend(fontsize=11, loc="upper right")
            plt.tight_layout()

            mu_tag = mu_s.replace(" ", "").replace("=", "").replace("^", "").replace("-", "m")
            fname = f"{D}/reliability_{scale}_mu{mu_tag}.png"
            plt.savefig(fname, dpi=150, bbox_inches="tight")
            plt.close()
            print(f"[OK] {T['saved']} {fname}")

    # ── PLOT 3: per ogni lambda fisso, sovrappone i 3 mu ─────────────────────
    for lam in sorted(lambdas):
        lam_s = lam_sym(lam)
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(T["inv_title"].format(lam=lam_s),
                     fontsize=14, fontweight="bold", color="#F1F5F9", y=0.99)

        for mu in mus:
            e   = get_exp(lam, mu)
            rv  = list(e[3:])
            rvc = [max(v, 1e-38) for v in rv]
            lbl = T["mu_legend"].format(mu=mu_sym(mu), exp=e[0])

            axes[0].plot(time_instants, rv, linestyle=MU_LINESTYLE[mu],
                         color=MU_COLORS_OV[mu], linewidth=2.8, marker="o", markersize=7, label=lbl)
            axes[1].plot(time_instants, rvc, linestyle=MU_LINESTYLE[mu],
                         color=MU_COLORS_OV[mu], linewidth=2.8, marker="o", markersize=7, label=lbl)

        axes[0].set_xlabel(T["time_xlabel"], fontsize=11)
        axes[0].set_ylabel(T["rel_ylabel"], fontsize=11)
        axes[0].set_ylim(-0.05, 1.05)
        axes[0].yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
        axes[0].grid(True); axes[0].legend(fontsize=10)
        axes[0].set_title(T["inv_lin"], color="#94A3B8", fontsize=11)

        axes[1].set_yscale("log")
        axes[1].set_xlabel(T["time_xlabel"], fontsize=11)
        axes[1].set_ylabel(T["log_ylabel"], fontsize=11)
        axes[1].grid(True, which="both", linestyle="--", alpha=0.3)
        axes[1].legend(fontsize=10)
        axes[1].set_title(T["inv_log"], color="#94A3B8", fontsize=11)

        plt.tight_layout()
        lam_tag = lam_s.replace(" ", "").replace("=", "").replace("^", "").replace("-", "m")
        fname = f"{D}/reliability_invariance_lam{lam_tag}.png"
        plt.savefig(fname, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"[OK] {T['saved']} {fname}")

    # ── PLOT 4: Heatmap a t=1080h ─────────────────────────────────────────────
    t_idx, t_val = 2, 1080
    lv = sorted(lambdas); mv = sorted(mus)
    RM = np.array([[get_exp(l, m)[3+t_idx] for l in lv] for m in mv])

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.suptitle(T["heat_title"].format(t=t_val),
                 fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)
    im = ax.imshow(RM, cmap="RdYlGn", vmin=0, vmax=1, aspect="auto", origin="lower")
    ax.set_xticks(range(len(lv))); ax.set_xticklabels([lam_sym(l) for l in lv], fontsize=11)
    ax.set_yticks(range(len(mv))); ax.set_yticklabels([mu_sym(m)  for m in mv], fontsize=11)
    ax.set_xlabel(T["heat_xlabel"], fontsize=12)
    ax.set_ylabel(T["heat_ylabel"], fontsize=12)
    exp_map = {(e[1],e[2]): e[0] for e in experiments_rel}
    for i, m in enumerate(mv):
        for j, l in enumerate(lv):
            v  = RM[i,j]; tc = "black" if 0.35 < v < 0.8 else "white"
            ax.text(j, i, f"Exp {exp_map[(l,m)]}\nR={v:.4f}",
                    ha="center", va="center", fontsize=10, fontweight="bold", color=tc)
    cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(f"Reliability R({t_val}h)", fontsize=11, color="#E2E8F0")
    cbar.ax.yaxis.set_tick_params(color="#94A3B8")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="#94A3B8")
    plt.tight_layout()
    plt.savefig(f"{D}/reliability_heatmap_{t_val}h.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {T['saved']} {D}/reliability_heatmap_{t_val}h.png")

    # ── PLOT 5: Bar chart, mu=0.01 di riferimento ─────────────────────────────
    mu_ref = 0.01
    mu_s   = mu_sym(mu_ref)
    fig, ax = plt.subplots(figsize=(11, 6))
    fig.suptitle(T["bar_title"].format(mu=mu_s),
                 fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)
    x, width, mult = np.arange(len(time_instants)), 0.25, 0
    for lam in sorted(lambdas):
        e   = get_exp(lam, mu_ref)
        rv  = list(e[3:])
        rvv = [max(v, 1e-4) for v in rv]
        lbl = T["lam_legend"].format(lam=lam_sym(lam), exp=e[0])
        ax.bar(x + width*mult, rvv, width, label=lbl,
               color=LAM_COLORS[lam], edgecolor="#475569", linewidth=0.7)
        mult += 1
    ax.set_ylabel(T["rel_ylabel"], fontsize=12)
    ax.set_xlabel(T["bar_xlabel"], fontsize=12)
    ax.set_xticks(x + width, [f"{t}h" for t in time_instants])
    ax.set_ylim(0, 1.15)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    ax.legend(loc='upper right', fontsize=11)
    mu_tag = mu_s.replace(" ", "").replace("=", "").replace("^", "").replace("-", "m")
    ax.text(0.01, 0.02, T["bar_note"], transform=ax.transAxes,
            fontsize=8, color="#94A3B8", alpha=0.8)
    plt.tight_layout()
    fname = f"{D}/reliability_barchart_mu{mu_tag}.png"
    plt.savefig(fname, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {T['saved']} {fname}")

print("\n[SUCCESS] Tutti i plot Reliability generati in ./plot/ita/ e ./plot/en/")

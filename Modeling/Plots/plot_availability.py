"""
Plot Availability in Regime Stazionario - Progetto Mobius
Genera i plot della sezione 3.1 del report e li salva in ./plot/ita e ./plot/en
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import cm

# ── Output dirs ───────────────────────────────────────────────────────────────
os.makedirs("plot/ita", exist_ok=True)
os.makedirs("plot/en",  exist_ok=True)

# ── Palette colori ────────────────────────────────────────────────────────────
MU_COLORS   = {0.01: "#2563EB", 0.001: "#16A34A", 1e-4: "#DC2626"}
MU_MARKERS  = {0.01: "o",       0.001: "s",        1e-4: "^"}
LAM_COLORS  = {0.01: "#7C3AED", 0.001: "#D97706",  1e-4: "#0D9488"}
LAM_MARKERS = {0.01: "o",       0.001: "s",         1e-4: "^"}

# ── Dati sperimentali ─────────────────────────────────────────────────────────
experiments = [
    (1,  0.01,   0.01,   0.333333, 0.222222),
    (2,  0.001,  0.01,   0.833333, 0.138889),
    (3,  1e-4,   0.01,   0.980392, 0.019223),
    (4,  0.01,   0.001,  0.047619, 0.045351),
    (5,  0.001,  0.001,  0.333333, 0.222222),
    (6,  1e-4,   0.001,  0.833333, 0.138889),
    (7,  0.01,   1e-4,   0.004975, 0.004950),
    (8,  0.001,  1e-4,   0.047619, 0.045351),
    (9,  1e-4,   1e-4,   0.333333, 0.222222),
]
lambdas = sorted(set(e[1] for e in experiments))
mus     = sorted(set(e[2] for e in experiments))

def get_avail(lam, mu):
    for e in experiments:
        if e[1] == lam and e[2] == mu:
            return e[3]

def get_var(lam, mu):
    for e in experiments:
        if e[1] == lam and e[2] == mu:
            return e[4]

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

# ── Helper: etichette con simboli ─────────────────────────────────────────────
def mu_tex(v):
    if v == 0.01:   return "\u03bc = 10\u207b\u00b2"
    if v == 0.001:  return "\u03bc = 10\u207b\u00b3"
    if v == 1e-4:   return "\u03bc = 10\u207b\u2074"

def lam_tex(v):
    if v == 0.01:   return "\u03bb = 10\u207b\u00b2"
    if v == 0.001:  return "\u03bb = 10\u207b\u00b3"
    if v == 1e-4:   return "\u03bb = 10\u207b\u2074"

def lam_tick(v):
    if v == 0.01:   return "10\u207b\u00b2"
    if v == 0.001:  return "10\u207b\u00b3"
    if v == 1e-4:   return "10\u207b\u2074"

TEXTS = {
    "ita": {
        "avail_label":  "Availability  A(\u221e)",
        "avail_title1": "Availability in Regime Stazionario\nvs Failure Rate \u03bb",
        "xlabel_lam":   "Failure Rate  \u03bb  [h\u207b\u00b9]",
        "avail_title2": "Availability in Regime Stazionario\nvs Repair Rate \u03bc",
        "xlabel_mu":    "Repair Rate  \u03bc  [h\u207b\u00b9]",
        "avail_title3": "Availability vs Rapporto di Carico  \u03c1 = \u03bb/\u03bc",
        "rho_label":    "A = 1/(1+\u03c1)  [teorico 1 comp.]",
        "xlabel_rho":   "\u03c1 = \u03bb/\u03bc  (rapporto guasto/riparazione)",
        "heatmap_title":    "Heatmap Availability A(\u221e) \u2014 Griglia \u03bb \u00d7 \u03bc",
        "barchart_title":   "Availability A(\u221e) \u2014 Confronto Esperimenti 1\u00f79",
        "saved": "Salvato:",
    },
    "en": {
        "avail_label":  "Availability  A(\u221e)",
        "avail_title1": "Steady-State Availability\nvs Failure Rate \u03bb",
        "xlabel_lam":   "Failure Rate  \u03bb  [h\u207b\u00b9]",
        "avail_title2": "Steady-State Availability\nvs Repair Rate \u03bc",
        "xlabel_mu":    "Repair Rate  \u03bc  [h\u207b\u00b9]",
        "avail_title3": "Availability vs Load Ratio  \u03c1 = \u03bb/\u03bc",
        "rho_label":    "A = 1/(1+\u03c1)  [theoretical 1 comp.]",
        "xlabel_rho":   "\u03c1 = \u03bb/\u03bc  (failure/repair ratio)",
        "heatmap_title":    "Heatmap Availability A(\u221e) \u2014 Grid \u03bb \u00d7 \u03bc",
        "barchart_title":   "Availability A(\u221e) \u2014 Experiments 1\u00f79 Comparison",
        "saved": "Saved:",
    },
}

for lang, T in TEXTS.items():
    D = f"plot/{lang}"

    # ── PLOT 1: A vs lambda, colore per mu ────────────────────────────────────
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.suptitle(T["avail_title1"], fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)
    for mu in sorted(mus, reverse=True):
        xs   = sorted(lambdas)
        ys   = [get_avail(l, mu) for l in xs]
        stds = [get_var(l, mu)**0.5 for l in xs]
        ax.plot(xs, ys, marker=MU_MARKERS[mu], linewidth=2.2, markersize=8,
                color=MU_COLORS[mu], label=mu_tex(mu), zorder=3)
        ax.fill_between(xs, [y-s for y,s in zip(ys,stds)],
                            [y+s for y,s in zip(ys,stds)],
                        alpha=0.15, color=MU_COLORS[mu])
    for exp, lam, mu, avail, _ in experiments:
        ax.annotate(f"Exp {exp}\n{avail:.3f}", xy=(lam, avail),
                    xytext=(5,6), textcoords="offset points",
                    fontsize=7.5, color="#CBD5E1", alpha=0.85)
    ax.set_xscale("log")
    ax.set_xlabel(T["xlabel_lam"], fontsize=11)
    ax.set_ylabel(T["avail_label"], fontsize=11)
    ax.set_ylim(-0.05, 1.05); ax.set_xlim(8e-5, 1.5e-2)
    ax.xaxis.set_major_formatter(ticker.LogFormatterSciNotation())
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    ax.grid(True); ax.legend(loc="upper right", fontsize=10)
    plt.tight_layout()
    plt.savefig(f"{D}/availability_vs_lambda.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {T['saved']} {D}/availability_vs_lambda.png")

    # ── PLOT 2: A vs mu, colore per lambda ────────────────────────────────────
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.suptitle(T["avail_title2"], fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)
    for lam in sorted(lambdas, reverse=True):
        xs   = sorted(mus)
        ys   = [get_avail(lam, m) for m in xs]
        stds = [get_var(lam, m)**0.5 for m in xs]
        ax.plot(xs, ys, marker=LAM_MARKERS[lam], linewidth=2.2, markersize=8,
                color=LAM_COLORS[lam], label=lam_tex(lam), zorder=3)
        ax.fill_between(xs, [y-s for y,s in zip(ys,stds)],
                            [y+s for y,s in zip(ys,stds)],
                        alpha=0.15, color=LAM_COLORS[lam])
    for exp, lam, mu, avail, _ in experiments:
        ax.annotate(f"Exp {exp}\n{avail:.3f}", xy=(mu, avail),
                    xytext=(5,6), textcoords="offset points",
                    fontsize=7.5, color="#CBD5E1", alpha=0.85)
    ax.set_xscale("log")
    ax.set_xlabel(T["xlabel_mu"], fontsize=11)
    ax.set_ylabel(T["avail_label"], fontsize=11)
    ax.set_ylim(-0.05, 1.05); ax.set_xlim(8e-5, 1.5e-2)
    ax.xaxis.set_major_formatter(ticker.LogFormatterSciNotation())
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    ax.grid(True); ax.legend(loc="upper left", fontsize=10)
    plt.tight_layout()
    plt.savefig(f"{D}/availability_vs_mu.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {T['saved']} {D}/availability_vs_mu.png")

    # ── PLOT 3: A vs rho ──────────────────────────────────────────────────────
    rhos   = [e[1]/e[2] for e in experiments]
    avails = [e[3]      for e in experiments]
    exps   = [e[0]      for e in experiments]
    rho_r  = np.logspace(-3, 3, 300)
    A_th   = 1.0 / (1.0 + rho_r)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.suptitle(T["avail_title3"], fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)
    ax.plot(rho_r, A_th, "--", color="#94A3B8", linewidth=1.5, label=T["rho_label"], zorder=2)
    sc = ax.scatter(rhos, avails, c=avails, cmap="RdYlGn", vmin=0, vmax=1,
                    s=120, zorder=4, edgecolors="#E2E8F0", linewidths=0.8)
    for rho, av, exp in zip(rhos, avails, exps):
        ax.annotate(f"Exp {exp}\n({av:.4f})", xy=(rho, av),
                    xytext=(8,4), textcoords="offset points",
                    fontsize=8, color="#CBD5E1")
    cbar = plt.colorbar(sc, ax=ax, pad=0.02)
    cbar.set_label(T["avail_label"], fontsize=10, color="#E2E8F0")
    cbar.ax.yaxis.set_tick_params(color="#94A3B8")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="#94A3B8")
    ax.set_xscale("log")
    ax.set_xlabel(T["xlabel_rho"], fontsize=11)
    ax.set_ylabel(T["avail_label"], fontsize=11)
    ax.set_ylim(-0.05, 1.05)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    ax.grid(True); ax.legend(loc="upper right", fontsize=10)
    plt.tight_layout()
    plt.savefig(f"{D}/availability_vs_rho.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {T['saved']} {D}/availability_vs_rho.png")

    # ── PLOT 4: Heatmap ───────────────────────────────────────────────────────
    lv = sorted(lambdas); mv = sorted(mus)
    AM = np.array([[get_avail(l, m) for l in lv] for m in mv])

    fig, ax = plt.subplots(figsize=(7, 6))
    fig.suptitle(T["heatmap_title"], fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)
    im = ax.imshow(AM, cmap="RdYlGn", vmin=0, vmax=1, aspect="auto", origin="lower")
    ax.set_xticks(range(len(lv))); ax.set_xticklabels([lam_tick(l) for l in lv], fontsize=11)
    ax.set_yticks(range(len(mv))); ax.set_yticklabels([lam_tick(m) for m in mv], fontsize=11)
    ax.set_xlabel(T["xlabel_lam"], fontsize=12)
    ax.set_ylabel(T["xlabel_mu"],  fontsize=12)
    exp_map = {(e[1],e[2]): e[0] for e in experiments}
    for i, m in enumerate(mv):
        for j, l in enumerate(lv):
            v = AM[i,j]; tc = "black" if 0.3 < v < 0.8 else "white"
            ax.text(j, i, f"Exp {exp_map[(l,m)]}\nA={v:.4f}",
                    ha="center", va="center", fontsize=9.5, fontweight="bold", color=tc)
    cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(T["avail_label"], fontsize=10, color="#E2E8F0")
    cbar.ax.yaxis.set_tick_params(color="#94A3B8")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="#94A3B8")
    plt.tight_layout()
    plt.savefig(f"{D}/availability_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {T['saved']} {D}/availability_heatmap.png")

    # ── PLOT 5: Bar chart ─────────────────────────────────────────────────────
    ea = [e[3]    for e in experiments]
    es = [e[4]**.5 for e in experiments]
    el = [f"Exp {e[0]}\n{lam_tick(e[1])}\n{lam_tick(e[2])}" for e in experiments]

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.suptitle(T["barchart_title"], fontsize=14, fontweight="bold", color="#F1F5F9", y=0.97)
    cmap_bar   = matplotlib.colormaps["RdYlGn"]
    bar_colors = [cmap_bar(a) for a in ea]
    bars = ax.bar(range(len(experiments)), ea, color=bar_colors, width=0.65,
                  zorder=3, edgecolor="#475569", linewidth=0.8)
    ax.errorbar(range(len(experiments)), ea, yerr=es, fmt="none",
                color="#94A3B8", capsize=5, capthick=1.5, elinewidth=1.5, zorder=4)
    for bar, av, std in zip(bars, ea, es):
        ax.text(bar.get_x()+bar.get_width()/2, av+std+0.015, f"{av:.4f}",
                ha="center", va="bottom", fontsize=8.5, fontweight="bold", color="#F1F5F9")
    ax.set_xticks(range(len(experiments))); ax.set_xticklabels(el, fontsize=8.5)
    ax.set_ylabel(T["avail_label"], fontsize=11)
    ax.set_ylim(0, 1.15)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    ax.grid(True, axis="y")
    ax.axhline(y=0.5, color="#64748B", linestyle=":", linewidth=1.2, label="A = 50%")
    ax.axhline(y=0.9, color="#3B82F6", linestyle=":", linewidth=1.2, label="A = 90%")
    ax.legend(fontsize=10, loc="upper right")
    plt.tight_layout()
    plt.savefig(f"{D}/availability_barchart.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {T['saved']} {D}/availability_barchart.png")

print("\n[SUCCESS] Tutti i plot Availability generati in ./plot/ita/ e ./plot/en/")

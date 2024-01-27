from ..utils import BasicSegment
from random import choice


class Segment(BasicSegment):
    good_emoji = [
        ":)", ":-)", ":D", ":-D", ":]", ":-]", ":)",
        ":-)", ":p", ":-p", ":P", ":-P", ";)", ";-)",
        '(˵ ͡° ͜ʖ ͡°˵)', '⊂(◉‿◉)つ', 'ʕ·͡ᴥ·ʔ', 'ʕっ•ᴥ•ʔっ',
        '( ͡° ᴥ ͡°)', 'ԅ(≖‿≖ԅ)', '(｡◕‿‿◕｡)', '(ღ˘⌣˘ღ)',
        ]
    bad_emoji = [
        ":(", ":-(", ":c", ":[", ":'(", ">:(", ">:[", ">:(|",
        '(ㆆ _ ㆆ)', 'ԅ(≖‿≖ԅ)', '☉ ‿ ⚆',
        '(͠≖ ͜ʖ͠≖)', '(¬,‿,¬)', '( ▀ ͜͞ʖ▀)'
        ]
    def add_to_powerline(self):
        powerline = self.powerline
        root_indicators = {
            'bash': ' \\$ ',
            'tcsh': ' %# ',
            'zsh': ' %# ',
            'bare': ' $ ',
        }
        bg = powerline.theme.CMD_PASSED_BG
        fg = powerline.theme.CMD_PASSED_FG
        emoji = choice(self.good_emoji)
        if powerline.args.prev_error != 0:
            fg = powerline.theme.CMD_FAILED_FG
            bg = powerline.theme.CMD_FAILED_BG
            emoji = choice(self.bad_emoji)
        powerline.append(f" {emoji} {root_indicators[powerline.args.shell]}", fg, bg, sanitize=False)

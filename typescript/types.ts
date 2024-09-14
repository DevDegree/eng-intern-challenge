type AllowedBraille = "O" | ".";
export type Braille =
  `${AllowedBraille}${AllowedBraille}${AllowedBraille}${AllowedBraille}${AllowedBraille}${AllowedBraille}`;

export type Utility = "capitalize" | "number" | "space";
export type Action = "capitalize" | "number" | "none";
